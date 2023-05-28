from dataclasses import dataclass
from typing import List
from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.max_beehives = max_beehives
        self.beehives = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.beehives = MaxHeap(self.max_beehives)
        for hive in hive_list:
            self.add_beehive(hive)
    
    def add_beehive(self, hive: Beehive):
        self.beehives.add(hive)

    
    def harvest_best_beehive(self):
        if len(self.beehives) == 0:
            raise IndexError("No beehives to harvest")

        best_hive = self.beehives.get_max()
        return best_hive
