#!/usr/bin/env python3
from typing import List


def sum_list(input_list: list[float]) -> float:
    total_list = 0
    for num in input_list:
        total_list += num
    return total_list
