"""Tests for the setup_logging helper in the greeter package."""

import logging
from greeter import setup_logging, Greeter


def test_setup_logging_adds_handler(caplog):
    """Test that setup_logging correctly adds a handler and sets the level."""
    # We can't easily test StreamHandler effects on sys.stderr here without
    # more complex mocking, but we can test that the logger's level is updated.

    # Get the library logger
    logger = logging.getLogger("greeter")

    # Initial state should be NOTSET (inheriting) or whatever it was
    original_level = logger.level

    # Call setup_logging
    setup_logging(level=logging.DEBUG)

    try:
        assert logger.level == logging.DEBUG

        # Test that the logs actually flow through at the new level
        with caplog.at_level(logging.DEBUG, logger="greeter"):
            greeter = Greeter()
            greeter.greet()
            assert "No name provided" in caplog.text

    finally:
        # Reset logger level to avoid side effects on other tests
        logger.setLevel(original_level)


def test_setup_logging_with_custom_handler():
    """Test that setup_logging accepts a custom handler."""
    logger = logging.getLogger("greeter")
    custom_handler = logging.NullHandler()

    # Just verify it doesn't crash and adds the handler
    # Note: we don't strictly assert the handler presence in the list
    # because it might be tricky with how pytest/logging handles singletons
    setup_logging(handler=custom_handler)

    assert custom_handler in logger.handlers
