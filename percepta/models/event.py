"""
Event model.

An Event represents a meaningful occurrence detected
by the system (motion, anomaly, reasoning result, etc.).
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import uuid


@dataclass
class Event:
    """
    Structured event emitted by processors.
    """

    # Unique identifier for this event
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    # Type of event (e.g., "motion_detected")
    event_type: str = ""

    # Timestamp in seconds
    timestamp: float = 0.0

    # Reference to frame or source index
    source_id: Optional[int] = None

    # Confidence score (0.0 to 1.0)
    confidence: Optional[float] = None

    # Additional event-specific information
    metadata: Dict[str, Any] = field(default_factory=dict)
