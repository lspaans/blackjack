"""Tests `Player`-class."""

import pytest

from blackjack import Player


def test_player(example_blackjack):
    """Tests constructor method."""
    assert isinstance(Player(example_blackjack), Player)
