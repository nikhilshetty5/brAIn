"""
Central configuration for the SDK.

All tunables live here so:
- customers can override easily
- no magic numbers are scattered
"""

from pathlib import Path


# Root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parents[2]


# Default video parameters
DEFAULT_FPS = 30
DEFAULT_FRAME_WIDTH = 1280
DEFAULT_FRAME_HEIGHT = 720


# FFmpeg executable path (can be overridden by user)
FFMPEG_BINARY = "ffmpeg"


# Logging
LOG_LEVEL = "INFO"
