# -*- coding: utf-8 -*-
# Game settings - Snake (tkinter version)

WINDOW_TITLE = "Snake"

CELL_SIZE   = 20      # pixels per cell
GRID_WIDTH  = 30      # cells horizontal
GRID_HEIGHT = 30      # cells vertical

CANVAS_WIDTH  = CELL_SIZE * GRID_WIDTH   # 600
CANVAS_HEIGHT = CELL_SIZE * GRID_HEIGHT  # 600

# Tick interval in ms (100 ms = 10 FPS)
TICK_MS      = 100
TICK_MIN_MS  = 40    # minimum interval (max speed)
SPEED_STEP   = 5     # reduce interval by 5 ms every 5 points

# Colors
COLOR_BG         = "#000000"
COLOR_GRID       = "#1e1e1e"
COLOR_FOOD       = "#dc2828"
COLOR_TEXT       = "#ffffff"
COLOR_OVERLAY_BG = "#111111"
COLOR_OBSTACLE        = "#8B4513"   # brown - inedible block
COLOR_OBSTACLE_BORDER = "#5C2D0A"

# Snake color palettes - changes on each food eaten
SNAKE_PALETTES = [
    ("#00dc00", "#00a000"),   # green (start)
    ("#00cfff", "#0088cc"),   # blue
    ("#ff9900", "#cc6600"),   # orange
    ("#cc44ff", "#8800cc"),   # purple
    ("#ff4488", "#cc0055"),   # pink
    ("#ffff00", "#bbbb00"),   # yellow
    ("#00ffcc", "#00aa88"),   # teal
    ("#ff6644", "#cc3300"),   # red-orange
]

# Obstacles
OBSTACLE_COUNT      = 10   # number of inedible blocks on the field
OBSTACLE_MIN_DIST   = 5    # minimum distance from snake start (in cells)

# Starting position (center)
SNAKE_START_X   = GRID_WIDTH  // 2
SNAKE_START_Y   = GRID_HEIGHT // 2
SNAKE_START_LEN = 3

# Directions (dx, dy)
DIR_UP    = (0, -1)
DIR_DOWN  = (0,  1)
DIR_LEFT  = (-1, 0)
DIR_RIGHT = (1,  0)

RECORD_FILE = "record.txt"
