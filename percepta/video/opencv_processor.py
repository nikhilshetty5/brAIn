"""
OpenCV-based frame processing.

This is where:
- resizing
- filtering
- motion analysis
will eventually live.
"""

import cv2
from percepta.models.frame import Frame
from percepta.utils.logger import get_logger

logger = get_logger(__name__)


class OpenCVProcessor:
    """
    Processes raw frames using OpenCV.
    """

    def process(self, frame: Frame) -> Frame:
        """
        Apply basic processing to a frame.

        Args:
            frame: Frame object

        Returns:
            Processed Frame
        """

        logger.debug(f"Processing frame {frame.frame_id}")

        # Example operation: convert to grayscale
        gray = cv2.cvtColor(frame.data, cv2.COLOR_BGR2GRAY)

        # Attach processed data as metadata
        frame.metadata = {
            "grayscale": gray
        }

        return frame
