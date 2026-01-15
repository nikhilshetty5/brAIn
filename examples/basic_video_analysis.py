from percepta.core.pipeline import Pipeline
from percepta.core.context import Context
from percepta.video.video_source import VideoSource
from percepta.processors.preprocess import PreprocessProcessor
from percepta.processors.motion import MotionProcessor

context = Context(api_key="demo-key")

source = VideoSource("sample.mp4")

processors = [
    PreprocessProcessor(),
    MotionProcessor()
]

pipeline = Pipeline(
    source=source,
    processors=processors,
    context=context
)

pipeline.run()
