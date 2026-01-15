"""
VideoSource using FFmpeg.

This source converts raw video frames into Frame objects
and yields them one by one to the Pipeline.
"""

from percepta.video.ffmpeg_reader import FFmpegVideoReader
from percepta.models.frame import Frame
from percepta.utils.logger import get_logger


class VideoSource:
    """
    Iterable video source backed by FFmpeg.
    """

    def __init__(self, video_path: str, fps: int = 30):
        self.video_path = video_path
        self.fps = fps
        self.reader = FFmpegVideoReader(video_path)
        self.frame_id = 0
        self.logger = get_logger(self.__class__.__name__)

    def __iter__(self):
        """
        Makes this class iterable.
        Pipeline will do: for frame in source
        """
        self.reader.start()
        return self

    def __next__(self) -> Frame:
        """
        Returns the next Frame.
        """
        raw_frame = self.reader.read_frame()

        if raw_frame is None:
            self.reader.stop()
            raise StopIteration

        frame = Frame(
            data=raw_frame,
            timestamp=self.frame_id / self.fps,
            frame_id=self.frame_id,
            metadata={}
        )

        self.frame_id += 1
        return frame
