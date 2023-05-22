from __future__ import annotations
from threedeebeetree import Point

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    def divide_points(points, axis):
        points.sort(key=lambda p: p[axis])
        mid = len(points) // 2
        return points[mid], points[:mid], points[mid + 1:]

    def create_ordered_list(points, axis):
        if len(points) == 0:
            return []
        elif len(points) == 1:
            return points
        else:
            root, left, right = divide_points(points, axis)
            return [root] + create_ordered_list(left, (axis + 1) % 3) + create_ordered_list(right, (axis + 1) % 3)

    return create_ordered_list(my_coordinate_list, 0)
