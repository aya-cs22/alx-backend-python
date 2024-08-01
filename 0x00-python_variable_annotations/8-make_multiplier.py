#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ takes a float multiplier as argument """
    def multiplier_func(x: float) -> float:
        return multiplier * x
    return multiplier_func
