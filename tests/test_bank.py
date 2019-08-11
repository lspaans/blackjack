"""Tests `bank`-class."""

import pytest

from blackjack import Bank


def test_bank(example_blackjack):
    """Tests constructor method."""
    assert isinstance(Bank(example_blackjack), Bank)
