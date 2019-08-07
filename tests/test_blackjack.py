"""Tests `BlackJack`-class."""

import pytest

from blackjack import BlackJack


def test_blackjack():
    """Tests constructor method with field values."""
    assert isinstance(BlackJack(), BlackJack)
