#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """takes a list mxd_lst of integers and floats """
    total_list = 0
    for num in mxd_lst:
        total_list += num
    return float(total_list)