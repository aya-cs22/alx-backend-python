#!/usr/bin/env python3
"""Complex types - list of floats"""
from typing import List


def sum_list(input_list: list[float]) -> float:
    """takes a list input_list of floats as argument"""
    total_list: float = 0.0
    for num in input_list:
        total_list += num
    return total_list
