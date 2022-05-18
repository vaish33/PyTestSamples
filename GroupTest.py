class TestClass:
    def test_one(self):
        x = "h"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "h")