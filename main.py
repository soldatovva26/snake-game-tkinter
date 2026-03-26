# -*- coding: utf-8 -*-
"""Entry point - Snake game on tkinter (no third-party libraries)."""

from game import Game


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
