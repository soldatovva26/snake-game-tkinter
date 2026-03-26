# Настройки игры «Змейка» (tkinter-версия)

WINDOW_TITLE = "Snake"

CELL_SIZE   = 20      # пикселей на клетку
GRID_WIDTH  = 30      # клеток по горизонтали
GRID_HEIGHT = 30      # клеток по вертикали

CANVAS_WIDTH  = CELL_SIZE * GRID_WIDTH   # 600
CANVAS_HEIGHT = CELL_SIZE * GRID_HEIGHT  # 600

# Интервал тика в мс (100 мс = 10 FPS)
TICK_MS      = 100
TICK_MIN_MS  = 40    # минимальный интервал (макс. скорость)
SPEED_STEP   = 5     # уменьшать интервал на 5 мс каждые 5 очков

# Цвета
COLOR_BG         = "#000000"
COLOR_GRID       = "#1e1e1e"
COLOR_SNAKE_HEAD = "#00dc00"
COLOR_SNAKE_BODY = "#00a000"
COLOR_FOOD       = "#dc2828"
COLOR_TEXT       = "#ffffff"
COLOR_OVERLAY_BG = "#111111"

# Начальная позиция (центр)
SNAKE_START_X   = GRID_WIDTH  // 2
SNAKE_START_Y   = GRID_HEIGHT // 2
SNAKE_START_LEN = 3

# Направления (dx, dy)
DIR_UP    = (0, -1)
DIR_DOWN  = (0,  1)
DIR_LEFT  = (-1, 0)
DIR_RIGHT = (1,  0)

RECORD_FILE = "record.txt"
