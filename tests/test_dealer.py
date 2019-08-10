"""Tests `Dealer`-class."""

import pytest

from blackjack import Dealer


def test_dealer(example_shoe):
    """Tests constructor method."""
    assert isinstance(Dealer(example_shoe), Dealer)
