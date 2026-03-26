# -*- coding: utf-8 -*-
"""Inedible obstacles on the field."""

import random
import math
from settings import (
    GRID_WIDTH, GRID_HEIGHT,
    SNAKE_START_X, SNAKE_START_Y,
    OBSTACLE_COUNT, OBSTACLE_MIN_DIST,
)


class Obstacles:
    """Generates and stores the list of inedible blocks."""

    def __init__(self, snake_body: list[tuple[int, int]]):
        self.cells: set[tuple[int, int]] = set()
        self.spawn(snake_body)

    def spawn(self, snake_body: list[tuple[int, int]]) -> None:
        """Places obstacles away from the snake start position."""
        self.cells = set()
        occupied = set(snake_body)

        candidates = [
            (x, y)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
            if (x, y) not in occupied
            and self._dist(x, y, SNAKE_START_X, SNAKE_START_Y) >= OBSTACLE_MIN_DIST
        ]

        count = min(OBSTACLE_COUNT, len(candidates))
        chosen = random.sample(candidates, count)
        self.cells = set(chosen)

    @staticmethod
    def _dist(x1: int, y1: int, x2: int, y2: int) -> float:
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
