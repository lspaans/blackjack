"""Tests `Dealer`-class."""

import pytest

from blackjack import Dealer


def test_dealer():
    """Tests constructor method with field values."""
    assert isinstance(Dealer(), Dealer)
