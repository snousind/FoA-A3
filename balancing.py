from __future__ import annotations

from ratio import Percentiles
from threedeebeetree import Point
from typing import List

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    """
    Best and Worst Case Complexity: O(n * log(n))

    This is because the complexity for sorting one point in the list based on their x, y and z
    coordinates is O(log(n)). However, there are n points in the list. Therefore, the complexity
    is O(n * log(n)).
    """

    x_sorted_values = sorted(my_coordinate_list, key=lambda p: p[0])
    y_sorted_values = sorted(my_coordinate_list, key=lambda p: p[1])
    z_sorted_values = sorted(my_coordinate_list, key=lambda p: p[2])
    return [point for points in zip(x_sorted_values, y_sorted_values, z_sorted_values) for point in points]
    #zip method combines a value from x, y and z







