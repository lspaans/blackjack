"""Tests `Shoe`-class."""

import pytest

from blackjack import Shoe


def test_shoe():
    """Tests constructor method with field values."""
    assert isinstance(Shoe(), Shoe)
