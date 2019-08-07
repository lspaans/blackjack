#!/usr/bin/env python3

import sys

from blackjack import BlackJack


def main():
    game = BlackJack()

    try:
        game.start()
    except KeyboardInterrupt as exc:
        sys.stderr.write("Game interrupted. Exiting!\n")

if __name__ == "__main__":
    sys.exit(main())
