from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    subtree_size: int = 1
    children: dict[int, BeeNode] = field(default_factory=dict)

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        """
        Constant time complexity of O(1) in both the best and worst cases.

        Regardless of the size of the children dictionary or the values stored in it, the time complexity of this code remains constant.
        """
        x, y, z = point
        octant = 0
        if x >= self.key[0]:
            octant |= 1
        if y >= self.key[1]:
            octant |= 2
        if z >= self.key[2]:
            octant |= 4
        return self.children.get(octant)



class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        """
        The best case complexity for this code is O(1) and the worst case complexity is O(log n), where n is the number of nodes in the tree.

        In the best case scenario, the desired node with the given key is the root node, and the code can directly return it without any further traversal or comparisons.
        This is a constant time operation, resulting in O(1) complexity.

        In the worst case scenario, the tree is a balanced binary search tree, and the desired node is located at the maximum depth of the tree.
        In this case, the code traverses the tree from the root to the desired node by following the appropriate child pointers at each level.
        Since the tree is balanced, the height of the tree is logarithmic to the number of nodes (n) in the tree.
        Therefore, the worst case complexity is O(log n).
        """
        if self.root is None:
            raise KeyError("Key not found")
        current = self.root
        while current:
            if current.key == key:
                return current
            child = current.get_child_for_key(key)
            if child is None:
                raise KeyError("Key not found")
            current = child

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        """
        The best and worst case complexity for this code can be analyzed as follows:

        Best Case Complexity:
        The best case occurs when the tree is empty, represented by the condition current is None at the beginning of the code.
        In this case, the code simply creates a new BeeNode with the given key and item.
        The complexity for this case is constant time, O(1), as it only involves creating a new node and updating the length.

        Worst Case Complexity:
        The worst case occurs when the tree is highly unbalanced and resembles a linked list.
        In this case, each insertion requires traversing the entire height of the tree to find the appropriate position to insert the node.
        The worst case time complexity for a binary tree is O(n), where n is the number of nodes.
        In the worst case, the complexity can be considered as O(n * log(n)), where n is the number of nodes and log(n) represents the average height of the octree.
        """
        if current is None:
            self.length += 1
            return BeeNode(key=key, item=item)

        x,y,z = key
        if key == current.key:
            current.item = item
        else:
            octant = 0
            if x >= current.key[0]:
                octant |= 1
            if y >= current.key[1]:
                octant |= 2
            if z >= current.key[2]:
                octant |= 4
            child = current.get_child_for_key(key)
            if child is None:
                child = BeeNode(key=key, item=item)
                current.children[octant] = child
            else:
                self.insert_aux(child, key, item)
            current.subtree_size += 1
        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        """
        The best-case complexity for this code is O(1) because it only requires a single operation to check if the current node has any children. 
        If the node has no children, the function immediately returns True.

        The worst-case complexity for this code is O(N), where N is the number of children in the current node. 
        In the worst case, the function needs to iterate through all the children of the node to determine if there are any. 
        However, if the code implementation internally keeps track of the number of children or has a direct reference to the children list, the worst-case complexity can be reduced to O(1).
        """
        return not current.children

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
