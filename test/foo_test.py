
from src.foo import foo1


class TestFoo:
    def test_foo(self):
        assert foo1() == 10

