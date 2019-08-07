"""Tests `Game`-class."""

import pytest

from blackjack import Game


def test_game():
    """Tests constructor method with field values."""
    assert isinstance(Game(), Game)
