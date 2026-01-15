"""
Motion detection processor.

Detects motion by comparing consecutive frames.
"""

import cv2
import numpy as np

from percepta.processors.base import Processor
from percepta.models.frame import Frame
from percepta.models.event import Event
from percepta.utils.logger import get_logger


class MotionProcessor(Processor):
    """
    Simple frame-difference based motion detector.
    """

    def __init__(self, threshold: float = 25.0):
        super().__init__(name="MotionProcessor")
        self.threshold = threshold
        self.prev_gray = None
        self.logger = get_logger(self.name)

    def initialize(self, context) -> None:
        self.logger.info("MotionProcessor initialized")

    def process(self, frame: Frame, context):
        events = []

        # Convert current frame to grayscale
        gray = cv2.cvtColor(frame.data, cv2.COLOR_BGR2GRAY)

        if self.prev_gray is not None:
            # Compute absolute difference
            diff = cv2.absdiff(self.prev_gray, gray)
            mean_diff = np.mean(diff)

            if mean_diff > self.threshold:
                event = Event(
                    event_type="motion_detected",
                    timestamp=frame.timestamp,
                    source_id=frame.frame_id,
                    confidence=min(mean_diff / 255.0, 1.0),
                    metadata={
                        "mean_difference": float(mean_diff)
                    }
                )
                events.append(event)

                self.logger.info(
                    f"Motion detected at frame {frame.frame_id}"
                )

        # Update previous frame
        self.prev_gray = gray

        return events

    def shutdown(self) -> None:
        self.logger.info("MotionProcessor shutdown")
