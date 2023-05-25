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
        return not current.children

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
