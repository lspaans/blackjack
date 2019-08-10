# flake8: noqa

"""Initializes `pytest` for `blackjack`-package."""

import pytest

from blackjack import exceptions, Bank, BlackJack, BlackJackCard, \
                      BlackJackPlayer,Dealer, Game, Hand, Player, Shoe


@pytest.fixture(scope="function")
def example_blackjack():
    """Returns instantiated example BlackJack game."""
    return BlackJack()

@pytest.fixture(scope="function")
def example_shoe():
    """Returns instantiated example Shoe."""
    return Shoe()
