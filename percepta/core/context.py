"""
Runtime context shared across the pipeline.
"""

from typing import Optional
from percepta.memory.event_buffer import EventBuffer


class Context:
    """
    Shared runtime context.

    Holds state that processors may need access to.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        customer_id: Optional[str] = None,
        max_events: int = 100
    ):
        # Identity / authentication (passed through, not validated here)
        self.api_key = api_key
        self.customer_id = customer_id

        # Short-term event memory
        self.event_buffer = EventBuffer(max_size=max_events)

        # Usage tracking (for future backend integration)
        self.events_processed = 0
