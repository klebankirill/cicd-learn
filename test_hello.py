from hello import greet
def test_greet_returns_correct_string():
    result = greet("world")
    assert result == "Hello, world!"
