#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    total_list = 0
    for num in mxd_lst:
        total_list += num
    return float(total_list)