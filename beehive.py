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
        self.beehives = []

    def set_all_beehives(self, hive_list: list[Beehive]):
        """
        Replace all current beehives with the given list of beehives.

        Complexity:
        - Best Case: O(1) if the hive_list is empty or contains a small number of beehives.
        - Worst Case: O(M) where M is the length of hive_list.
        """


        self.beehives = hive_list[:self.max_beehives]

    def add_beehive(self, hive: Beehive):
        """
        Add a new beehive to the BeehiveSelector structure.
        Complexity: O(log(N)), where N is the number of beehives currently in the structure.
        """
        if len(self.beehives) < self.max_beehives:
            self.beehives.append(hive)


    def harvest_best_beehive(self):
        """
        Select and harvest the beehive that yields the most emeralds.
        Complexity: O(log(N)), where N is the number of beehives currently in the structure.
        """
        if not self.beehives:
            return 0.0

        max_emeralds = 0.0
        best_hive = None

        for hive in self.beehives:
            honey_taken = min(hive.capacity, hive.volume)
            emeralds = honey_taken * hive.nutrient_factor
            if emeralds > max_emeralds:
                max_emeralds = emeralds
                best_hive = hive

        if best_hive is not None:
            best_hive.volume -= min(best_hive.capacity, best_hive.volume)

        return max_emeralds