"""Tests `Hand`-class."""

import pytest

from blackjack import Hand


def test_hand():
    """Tests constructor method with field values."""
    assert isinstance(Hand(), Hand)
