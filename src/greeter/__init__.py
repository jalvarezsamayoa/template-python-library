import logging

__version__ = "0.1.0"

# Set up NullHandler to prevent "No handler found" warnings
# if the consuming application doesn't configure logging.
logging.getLogger(__name__).addHandler(logging.NullHandler())

from .greeter import Greeter

__all__ = ["Greeter"]
