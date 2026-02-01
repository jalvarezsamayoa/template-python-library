"""Initialization for the greeter package."""

import logging

from .greeter import Greeter

__version__ = "0.1.0"

# Set up NullHandler to prevent "No handler found" warnings
# if the consuming application doesn't configure logging.
logging.getLogger(__name__).addHandler(logging.NullHandler())

__all__ = ["Greeter"]
