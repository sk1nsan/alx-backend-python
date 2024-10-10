#!/usr/bin/env python3
""" Complex types - functions """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function """
    def f(x: float) -> float:
        return x * multiplier
    return f
