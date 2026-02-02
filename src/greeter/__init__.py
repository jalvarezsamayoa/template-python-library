"""Initialization for the greeter package."""

import logging
from typing import Optional

from .greeter import Greeter

__version__ = "0.1.0"

# Set up NullHandler to prevent "No handler found" warnings
# if the consuming application doesn't configure logging.
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def setup_logging(
    level: int = logging.INFO, handler: Optional[logging.Handler] = None
) -> None:
    """
    Convenience function to set up logging for the greeter library.

    This is similar to boto3's set_stream_logger(). It helps users quickly
    see what the library is doing without manual logging configuration.

    Args:
        level: The logging level to use (e.g., logging.DEBUG, logging.INFO).
        handler: An optional handler to add. If None, a StreamHandler is added.
    """
    if handler is None:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

    logger.setLevel(level)
    logger.addHandler(handler)


__all__ = ["Greeter", "setup_logging"]
