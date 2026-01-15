"""
Base processor contract.

All processors in the SDK must inherit from this class.
"""

from abc import ABC, abstractmethod
from typing import List

from percepta.models.frame import Frame
from percepta.models.event import Event


class Processor(ABC):
    """
    Abstract base class for all processors.

    A processor:
    - receives a Frame
    - may generate zero or more Events
    - does not control pipeline execution
    """

    def __init__(self, name: str):
        self.name = name

    def initialize(self, context) -> None:
        """
        Called once before the pipeline starts.

        Override if the processor needs setup.
        """
        pass

    @abstractmethod
    def process(self, frame: Frame, context) -> List[Event]:
        """
        Process a single frame.

        Must be implemented by all processors.

        Args:
            frame: Time-stamped Frame
            context: Shared runtime context

        Returns:
            List of Events (can be empty)
        """
        pass

    def shutdown(self) -> None:
        """
        Called once when the pipeline shuts down.

        Override if cleanup is required.
        """
        pass
