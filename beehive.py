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
        self.beehives = MaxHeap(max_size=max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.beehives.clear()
        for hive in hive_list:
            self.beehives.insert((-hive.capacity * hive.nutrient_factor, hive))
    
    def add_beehive(self, hive: Beehive):
        if len(self.beehives) < self.max_beehives:
            self.beehives.insert((-hive.capacity * hive.nutrient_factor, hive))
        else:
            # Replace the beehive with the lowest emerald value if the heap is full
            if self.beehives.root_key() < -hive.capacity * hive.nutrient_factor:
                self.beehives.extract_root()
                self.beehives.insert((-hive.capacity * hive.nutrient_factor, hive))
    
    def harvest_best_beehive(self):
        if not self.beehives:
            return 0.0

        _, best_hive = self.beehives.extract_root()
        honey_taken = min(best_hive.capacity, best_hive.volume)
        emeralds = honey_taken * best_hive.nutrient_factor
        best_hive.volume -= honey_taken

        if best_hive.volume > 0:
            self.beehives.insert((-best_hive.capacity * best_hive.nutrient_factor, best_hive))

        return emeralds


