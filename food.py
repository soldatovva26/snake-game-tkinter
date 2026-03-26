"""Логика еды."""

import random
from settings import GRID_WIDTH, GRID_HEIGHT


class Food:
    def __init__(self, snake_body: list[tuple[int, int]]):
        self.position: tuple[int, int] = (0, 0)
        self.spawn(snake_body)

    def spawn(self, snake_body: list[tuple[int, int]]):
        """Генерирует еду в свободной клетке."""
        occupied = set(snake_body)
        free = [
            (x, y)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
            if (x, y) not in occupied
        ]
        if free:
            self.position = random.choice(free)
