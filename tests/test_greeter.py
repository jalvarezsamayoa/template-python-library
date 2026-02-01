from greeter import Greeter


def test_greet_world():
    """Test greeting the world (default)."""
    greeter = Greeter()
    assert greeter.greet() == "Hello World"


def test_greet_name():
    """Test greeting a specific name."""
    greeter = Greeter()
    assert greeter.greet("Alice") == "Hello Alice"
