"""Tests `Deck`-class."""

import pytest

from blackjack import Deck


def test_deck():
    """Tests constructor method with field values."""
    assert isinstance(Deck(), Deck)
