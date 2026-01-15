"""
Pipeline module.

The Pipeline is responsible for:
- controlling execution flow
- passing data through processors
- managing shared context
- collecting events

It does NOT contain business logic or AI logic.
"""

from typing import List, Iterable

from percepta.models.frame import Frame
from percepta.core.context import Context
from percepta.processors.base import Processor
from percepta.utils.logger import get_logger


class Pipeline:
    """
    Core pipeline orchestrator.

    The pipeline:
    - pulls data from a source
    - passes it through processors in order
    - stores generated events in context
    """

    def __init__(
        self,
        source: Iterable[Frame],
        processors: List[Processor],
        context: Context,
    ):
        """
        Initialize the pipeline.

        Args:
            source: Iterable source of Frames (video, sensor, etc.)
            processors: List of processors to run sequentially
            context: Shared runtime context
        """
        self.source = source
        self.processors = processors
        self.context = context
        self.logger = get_logger(self.__class__.__name__)

    def initialize(self) -> None:
        """
        Initialize pipeline and all processors.
        """
        self.logger.info("Initializing pipeline")

        for processor in self.processors:
            processor.initialize(self.context)

    def run(self) -> None:
        """
        Run the pipeline end-to-end.
        """
        self.initialize()

        for frame in self.source:
            self.process_frame(frame)

        self.shutdown()

    def process_frame(self, frame: Frame) -> None:
        """
        Process a single frame through all processors.

        Args:
            frame: A single time-stamped Frame
        """
        for processor in self.processors:
            events = processor.process(frame, self.context)

            # Store generated events in shared memory
            for event in events:
                self.context.event_buffer.add(event)
                self.context.events_processed += 1

    def shutdown(self) -> None:
        """
        Shutdown pipeline and all processors cleanly.
        """
        self.logger.info("Shutting down pipeline")

        for processor in self.processors:
            processor.shutdown()
