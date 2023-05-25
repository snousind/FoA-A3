from __future__ import annotations

import bisect
from typing import Generic, TypeVar, List, Set
from math import ceil
from bst import BinarySearchTree
from node import TreeNode

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.points = []
    
    def add_point(self, item: T):
        """
        Best Case Complexity: O(log(N))
        This occurs when the insertion point is in the middle of this list,
        which does not require elements to shift.

        Worst Case Complexity: O(N)
        This occurs when the insertion point is either at the beginning or end
        of a list, thus requiring elements to shift.
        """
        #self.points.append(item) #alternative code using lists
        bisect.insort(self.points, item)

    
    def remove_point(self, item: T):
        #self.points.remove(item) #alternative code using lists
        """
        Best Case Complexity: O(log(N))
        This occurs when the point is not in the list.

        Worst Case Complexity: O(N)
        This occurs when the point is at the end of the list. When this happens, all
        elements in the list are shifted.
        """
        index = bisect.bisect_left(self.points, item)
        if index < len(self.points) and self.points[index] == item:
            del self.points[index]


    def ratio(self, x, y):
        """
        Best Case Complexity: O(N * log(N))
        This occurs when N (the total number of points currently in the Percentile object)
        is small and O (the number of points returned by the function) is small in comparison
        to N.

        Worst Case Complexity: O(N * log(N) + O)
        This occurs when N (the total number of points currently in the Percentile object)
        is large and O (the number of points returned by the function) is close to N.
        """
        n = len(self.points)
        lower_rank = ceil(n * x / 100)
        upper_rank = n - ceil(n * y / 100)
        sorted_points = sorted(self.points)
        return sorted_points[lower_rank:upper_rank]


if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
