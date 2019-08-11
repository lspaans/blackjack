#!/usr/bin/env python3

import argparse
import logging
import sys

from blackjack import BlackJack


def get_arguments():
    arguments = argparse.ArgumentParser()

    arguments.add_argument("-d", "--debug", action="store_true",
                           help='Write debugging output to stderr')

    return arguments.parse_args()


def main():
    arguments = get_arguments()
    logger = logging.getLogger(__name__)

    if arguments.debug is True:
        logger.addHandler(logging.StreamHandler(sys.stderr))
        logger.setLevel(logging.DEBUG)
    else:
        logger.addHandler(logging.NullHandler())

    try:
        BlackJack(logger_name=__name__).start()
    except KeyboardInterrupt:
        logger.warning("Game interrupted. Exiting!")


if __name__ == "__main__":
    sys.exit(main())
