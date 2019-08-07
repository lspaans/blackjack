"""Tests `bank`-class."""

import pytest

from blackjack import Bank


def test_bank():
    """Tests constructor method with field values."""
    assert isinstance(Bank(), Bank)
