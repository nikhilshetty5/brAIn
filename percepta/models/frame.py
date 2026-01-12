"""
Data model representing a single video frame.

Models act as contracts between modules.
"""

from dataclasses import dataclass
import numpy as np
from typing import Optional


@dataclass
class Frame:
    """
    Represents a decoded video frame.

    Attributes:
        data: Raw image data (OpenCV format)
        timestamp: Timestamp in seconds
        frame_id: Sequential frame number
    """

    data: np.ndarray
    timestamp: float
    frame_id: int
    metadata: Optional[dict] = None
