"""Точка входа — змейка на tkinter (без сторонних библиотек)."""

from game import Game


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
