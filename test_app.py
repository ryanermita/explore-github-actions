import app
import pytest


def test_is_add():
    assert app.is_odd(2) == True


def test_is_even():
    assert app.is_odd(3) == False
