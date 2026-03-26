# -*- coding: utf-8 -*-
"""Food logic."""

import random
from settings import GRID_WIDTH, GRID_HEIGHT


class Food:
    def __init__(self, snake_body: list[tuple[int, int]],
                 obstacles: set[tuple[int, int]] | None = None):
        self.position: tuple[int, int] = (0, 0)
        self.spawn(snake_body, obstacles)

    def spawn(self, snake_body: list[tuple[int, int]],
              obstacles: set[tuple[int, int]] | None = None) -> None:
        """Spawns food in a free cell (not on snake or obstacle)."""
        occupied = set(snake_body) | (obstacles if obstacles else set())
        free = [
            (x, y)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
            if (x, y) not in occupied
        ]
        if free:
            self.position = random.choice(free)
