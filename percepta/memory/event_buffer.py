"""
Short-term in-memory buffer for events.
"""

from collections import deque
from typing import List
from percepta.models.event import Event


class EventBuffer:
    """
    Stores a fixed number of recent events.
    """

    def __init__(self, max_size: int = 100):
        self._buffer = deque(maxlen=max_size)

    def add(self, event: Event) -> None:
        self._buffer.append(event)

    def get_recent(self) -> List[Event]:
        return list(self._buffer)

    def clear(self) -> None:
        self._buffer.clear()
