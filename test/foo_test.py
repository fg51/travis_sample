#coding: utf-8

from src.foo import foo

class TestFoo:
    def test_foo(self):

        assert foo() == 10
