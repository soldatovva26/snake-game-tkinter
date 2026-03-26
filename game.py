"""Игровой цикл и отрисовка на tkinter Canvas."""

import tkinter as tk
from tkinter import font as tkfont

from settings import (
    WINDOW_TITLE,
    CELL_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT,
    TICK_MS, TICK_MIN_MS, SPEED_STEP,
    COLOR_BG, COLOR_GRID,
    COLOR_SNAKE_HEAD, COLOR_SNAKE_BODY, COLOR_FOOD,
    COLOR_TEXT, COLOR_OVERLAY_BG,
    DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT,
    RECORD_FILE,
)
from snake import Snake
from food import Food


class Game:
    """Управляет окном, Canvas и игровым циклом."""

    def __init__(self):
        # --- окно ---
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.resizable(False, False)
        self.root.configure(bg=COLOR_BG)

        # --- Canvas ---
        self.canvas = tk.Canvas(
            self.root,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            bg=COLOR_BG,
            highlightthickness=0,
        )
        self.canvas.pack()

        # --- шрифты ---
        self.font_hud   = tkfont.Font(family="Courier", size=14, weight="bold")
        self.font_big   = tkfont.Font(family="Courier", size=36, weight="bold")
        self.font_small = tkfont.Font(family="Courier", size=16)

        # --- состояние ---
        self.record   = self._load_record()
        self.tick_ms  = TICK_MS
        self.paused   = False
        self.game_over = False
        self._after_id = None

        self._new_game()

        # --- привязка клавиш ---
        self.root.bind("<Up>",     lambda e: self.snake.change_direction(DIR_UP))
        self.root.bind("<Down>",   lambda e: self.snake.change_direction(DIR_DOWN))
        self.root.bind("<Left>",   lambda e: self.snake.change_direction(DIR_LEFT))
        self.root.bind("<Right>",  lambda e: self.snake.change_direction(DIR_RIGHT))
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind("<space>",  lambda e: self._toggle_pause())
        self.root.bind("<r>",      lambda e: self._restart())
        self.root.bind("<R>",      lambda e: self._restart())

    # ------------------------------------------------------------------
    # Запуск
    # ------------------------------------------------------------------

    def run(self):
        self._schedule_tick()
        self.root.mainloop()
        self._save_record()

    # ------------------------------------------------------------------
    # Внутренние методы
    # ------------------------------------------------------------------

    def _new_game(self):
        self.snake     = Snake()
        self.food      = Food(self.snake.body)
        self.score     = 0
        self.tick_ms   = TICK_MS
        self.paused    = False
        self.game_over = False

    def _restart(self):
        if self._after_id:
            self.root.after_cancel(self._after_id)
        self._new_game()
        self._schedule_tick()

    def _toggle_pause(self):
        if not self.game_over:
            self.paused = not self.paused

    def _schedule_tick(self):
        self._after_id = self.root.after(self.tick_ms, self._tick)

    def _tick(self):
        if not self.paused and not self.game_over:
            self._update()
        self._draw()
        self._schedule_tick()

    # ------------------------------------------------------------------
    # Обновление состояния
    # ------------------------------------------------------------------

    def _update(self):
        self.snake.move()

        # Столкновения
        if self.snake.check_wall_collision() or self.snake.check_self_collision():
            self.game_over = True
            if self.score > self.record:
                self.record = self.score
                self._save_record()
            return

        # Еда
        if self.snake.head == self.food.position:
            self.snake.grow()
            self.score += 1
            self.food.spawn(self.snake.body)

            # Ускорение каждые 5 очков
            if self.score % 5 == 0:
                self.tick_ms = max(self.tick_ms - SPEED_STEP, TICK_MIN_MS)

    # ------------------------------------------------------------------
    # Отрисовка
    # ------------------------------------------------------------------

    def _draw(self):
        self.canvas.delete("all")
        self._draw_grid()
        self._draw_food()
        self._draw_snake()
        self._draw_hud()

        if self.paused and not self.game_over:
            self._draw_overlay("ПАУЗА", "SPACE — продолжить")

        if self.game_over:
            self._draw_overlay("GAME OVER", "R — новая игра   ESC — выход")

    def _draw_grid(self):
        for x in range(0, CANVAS_WIDTH, CELL_SIZE):
            self.canvas.create_line(x, 0, x, CANVAS_HEIGHT, fill=COLOR_GRID)
        for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
            self.canvas.create_line(0, y, CANVAS_WIDTH, y, fill=COLOR_GRID)

    def _draw_snake(self):
        for i, (cx, cy) in enumerate(self.snake.body):
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE_BODY
            x1 = cx * CELL_SIZE + 1
            y1 = cy * CELL_SIZE + 1
            x2 = x1 + CELL_SIZE - 2
            y2 = y1 + CELL_SIZE - 2
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def _draw_food(self):
        fx, fy = self.food.position
        x1 = fx * CELL_SIZE + 3
        y1 = fy * CELL_SIZE + 3
        x2 = x1 + CELL_SIZE - 6
        y2 = y1 + CELL_SIZE - 6
        self.canvas.create_oval(x1, y1, x2, y2, fill=COLOR_FOOD, outline="")

    def _draw_hud(self):
        text = f"Score: {self.score}   Best: {self.record}"
        # тень
        self.canvas.create_text(9, 9, anchor="nw", text=text,
                                 font=self.font_hud, fill="#000000")
        self.canvas.create_text(8, 8, anchor="nw", text=text,
                                 font=self.font_hud, fill=COLOR_TEXT)

    def _draw_overlay(self, title: str, hint: str):
        # полупрозрачный фон — имитируем через тёмный прямоугольник
        pad = 20
        cx, cy = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2

        # рамка
        self.canvas.create_rectangle(
            pad, cy - 70, CANVAS_WIDTH - pad, cy + 70,
            fill=COLOR_OVERLAY_BG, outline="#444444", width=2,
        )

        # заголовок
        self.canvas.create_text(cx, cy - 20, text=title,
                                 font=self.font_big, fill=COLOR_TEXT)
        # подсказка
        self.canvas.create_text(cx, cy + 35, text=hint,
                                 font=self.font_small, fill="#aaaaaa")

    # ------------------------------------------------------------------
    # Рекорд
    # ------------------------------------------------------------------

    def _load_record(self) -> int:
        try:
            with open(RECORD_FILE) as f:
                return int(f.read().strip())
        except (FileNotFoundError, ValueError):
            return 0

    def _save_record(self):
        with open(RECORD_FILE, "w") as f:
            f.write(str(self.record))
