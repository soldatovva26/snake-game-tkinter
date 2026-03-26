# -*- coding: utf-8 -*-
"""Snake logic."""

from settings import (
    SNAKE_START_X, SNAKE_START_Y, SNAKE_START_LEN,
    DIR_RIGHT, GRID_WIDTH, GRID_HEIGHT,
    SNAKE_PALETTES,
)


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.body: list[tuple[int, int]] = [
            (SNAKE_START_X - i, SNAKE_START_Y)
            for i in range(SNAKE_START_LEN)
        ]
        self.direction = DIR_RIGHT
        self._next_dir = DIR_RIGHT
        self._grow     = False

        # Color palette: index into SNAKE_PALETTES
        self._palette_index = 0
        self.color_head, self.color_body = SNAKE_PALETTES[0]

    # --- public API ---------------------------------------------------

    def change_direction(self, new_dir: tuple[int, int]):
        """Prevents 180-degree reversal."""
        opposite = (-self.direction[0], -self.direction[1])
        if new_dir != opposite:
            self._next_dir = new_dir

    def move(self):
        self.direction = self._next_dir
        hx, hy = self.body[0]
        dx, dy = self.direction
        self.body.insert(0, (hx + dx, hy + dy))
        if self._grow:
            self._grow = False
        else:
            self.body.pop()

    def grow(self):
        self._grow = True

    def next_color(self):
        """Switches to the next color palette when food is eaten."""
        self._palette_index = (self._palette_index + 1) % len(SNAKE_PALETTES)
        self.color_head, self.color_body = SNAKE_PALETTES[self._palette_index]

    def check_wall_collision(self) -> bool:
        hx, hy = self.body[0]
        return hx < 0 or hx >= GRID_WIDTH or hy < 0 or hy >= GRID_HEIGHT

    def check_self_collision(self) -> bool:
        return self.body[0] in self.body[1:]

    def check_obstacle_collision(self, obstacles: set[tuple[int, int]]) -> bool:
        """Returns True if the head hits an obstacle."""
        return self.body[0] in obstacles

    @property
    def head(self) -> tuple[int, int]:
        return self.body[0]
