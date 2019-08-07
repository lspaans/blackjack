"""Tests `Player`-class."""

import pytest

from blackjack import Player


def test_player():
    """Tests constructor method with field values."""
    assert isinstance(Player(), Player)
