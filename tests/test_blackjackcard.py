"""Tests `BlackJackCard`-class."""

import pytest

from blackjack import BlackJackCard


def test_blackjackcard():
    """Tests constructor method with field values."""
    assert isinstance(BlackJackCard(), BlackJackCard)
