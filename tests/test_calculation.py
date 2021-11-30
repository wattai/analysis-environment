# -*- coding: utf-8 -*-

import pytest

from sample.calculation import add, sub


@pytest.mark.parametrize("a", [-1, 0, 1])
@pytest.mark.parametrize("b", [-1, 0, 1])
def test_add(a, b):
    assert add(a, b) == a + b


@pytest.mark.parametrize("a", [-1, 0, 1])
@pytest.mark.parametrize("b", [-1, 0, 1])
def test_sub(a, b):
    assert sub(a, b) == a - b
