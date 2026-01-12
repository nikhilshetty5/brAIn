"""
Processing pipeline.

Pipelines define:
input → processing → output
"""

from percepta.video.ffmpeg_reader import FFmpegVideoReader
from percepta.video.opencv_processor import OpenCVProcessor
from percepta.models.frame import Frame
from percepta.utils.logger import get_logger

logger = get_logger(__name__)


class VideoPipeline:
    """
    Orchestrates video ingestion and processing.
    """

    def __init__(self, video_path: str):
        self.reader = FFmpegVideoReader(video_path)
        self.processor = OpenCVProcessor()
        self.frame_id = 0

    def run(self):
        """
        Run the full pipeline.
        """

        self.reader.start()

        while True:
            raw_frame = self.reader.read_frame()
            if raw_frame is None:
                break

            frame = Frame(
                data=raw_frame,
                timestamp=self.frame_id / 30.0,
                frame_id=self.frame_id
            )

            processed = self.processor.process(frame)

            logger.info(f"Processed frame {processed.frame_id}")
            self.frame_id += 1

        self.reader.stop()
