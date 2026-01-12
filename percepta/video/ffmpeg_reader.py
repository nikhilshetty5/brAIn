"""
FFmpeg-based video reader.

Purpose:
- Efficiently decode video streams
- Abstract FFmpeg complexity away from users
"""

import subprocess
import numpy as np
from percepta.utils.logger import get_logger
from percepta.config.settings import (
    FFMPEG_BINARY,
    DEFAULT_FRAME_WIDTH,
    DEFAULT_FRAME_HEIGHT,
)

logger = get_logger(__name__)


class FFmpegVideoReader:
    """
    Reads raw frames from a video file using FFmpeg.
    """

    def __init__(self, video_path: str):
        self.video_path = video_path
        self.process = None

    def start(self):
        """
        Starts FFmpeg subprocess to stream raw frames.
        """

        logger.info(f"Starting FFmpeg for {self.video_path}")

        self.process = subprocess.Popen(
            [
                FFMPEG_BINARY,
                "-i", self.video_path,
                "-f", "rawvideo",
                "-pix_fmt", "bgr24",
                "-"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        )

    def read_frame(self):
        """
        Reads a single frame from FFmpeg stdout.

        Returns:
            Numpy array or None if stream ended
        """

        frame_size = DEFAULT_FRAME_WIDTH * DEFAULT_FRAME_HEIGHT * 3
        raw_bytes = self.process.stdout.read(frame_size)

        if len(raw_bytes) != frame_size:
            return None

        frame = np.frombuffer(raw_bytes, dtype=np.uint8)
        frame = frame.reshape(
            (DEFAULT_FRAME_HEIGHT, DEFAULT_FRAME_WIDTH, 3)
        )

        return frame

    def stop(self):
        """
        Terminates FFmpeg process.
        """

        if self.process:
            logger.info("Stopping FFmpeg")
            self.process.terminate()
