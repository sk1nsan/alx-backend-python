#!/usr/bin/env python3
""" Complex types - mixed list """

from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """ returns their sum as a float """
    return float(sum(mxd_lst))
