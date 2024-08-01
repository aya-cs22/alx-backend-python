#!/usr/bin/env python3
from typing import Union


def sum_mixed_list(mxd_lst: list[float, int]) -> float:
    total_list = 0
    for num in mxd_lst:
        total_list += num
    return total_list