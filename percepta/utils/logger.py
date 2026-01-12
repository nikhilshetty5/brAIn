"""
Centralized logging utility.

Why this exists:
- consistent logs across modules
- easy integration into customer logging infra
"""

import logging
from percepta.config.settings import LOG_LEVEL


def get_logger(name: str) -> logging.Logger:
    """
    Creates or returns a named logger.

    Args:
        name: module name using the logger

    Returns:
        Configured logger instance
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers when imported multiple times
    if not logger.handlers:
        logger.setLevel(LOG_LEVEL)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
