"""Main module for the greeter package."""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class Greeter:
    """A simple class to greet the world."""

    def greet(self, name: Optional[str] = None) -> str:
        """
        Greet someone or the world.

        Args:
            name: The name to greet. If None, greets the world.

        Returns:
            A greeting string.
        """
        if name is None:
            logger.debug("No name provided, falling back to default")
            return "Hello World"

        logger.info("Greeting user: %s", name)
        return f"Hello {name}"
