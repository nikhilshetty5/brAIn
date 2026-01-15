"""
Preprocess processor.

This processor performs basic frame preprocessing
(e.g., grayscale conversion) and stores results in metadata.
"""

import cv2

from percepta.processors.base import Processor
from percepta.models.frame import Frame
from percepta.models.event import Event
from percepta.utils.logger import get_logger


class PreprocessProcessor(Processor):
    """
    Basic preprocessing processor.

    Responsibilities:
    - prepare frame data
    - enrich frame metadata
    - do NOT produce events
    """

    def __init__(self):
        super().__init__(name="PreprocessProcessor")
        self.logger = get_logger(self.name)

    def initialize(self, context) -> None:
        """
        Called once before processing starts.
        """
        self.logger.info("PreprocessProcessor initialized")

    def process(self, frame: Frame, context):
        """
        Process a single frame.

        Args:
            frame: Frame to preprocess
            context: Shared runtime context

        Returns:
            Empty list (no events generated)
        """

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame.data, cv2.COLOR_BGR2GRAY)

        # Store processed output in frame metadata
        frame.metadata = frame.metadata or {}
        frame.metadata["grayscale"] = gray

        self.logger.debug(
            f"Frame {frame.frame_id} preprocessed (grayscale)"
        )

        # Preprocessing does not generate events
        return []

    def shutdown(self) -> None:
        """
        Called once when pipeline shuts down.
        """
        self.logger.info("PreprocessProcessor shutdown")
