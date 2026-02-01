"""Tests for the logging behavior of the Greeter class."""

import logging
from greeter import Greeter


def test_greeting_logs_info(caplog):
    """Test that greeting with a name logs at INFO level."""
    caplog.set_level(logging.INFO)

    greeter = Greeter()
    greeter.greet("Alice")

    # Assert that the specific log message exists
    assert "Greeting user: Alice" in caplog.text

    # Assert it was logged at the correct level using records
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "INFO"


def test_default_greeting_logs_debug(caplog):
    """Test that default greeting logs at DEBUG level."""
    # Ensure we capture DEBUG logs
    caplog.set_level(logging.DEBUG)

    greeter = Greeter()
    greeter.greet()

    assert "No name provided, falling back to default" in caplog.text
    assert caplog.records[0].levelname == "DEBUG"
