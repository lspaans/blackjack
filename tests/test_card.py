"""Tests `Card`-class."""

import pytest

from blackjack import Card


@pytest.mark.parametrize("suite_symbol", Card.SUITE_SYMBOLS) 
@pytest.mark.parametrize("face_symbol", Card.FACE_SYMBOLS) 
def test_card_using_symbols(face_symbol, suite_symbol):
    """Tests constructor method."""
    assert isinstance(Card(face_symbol, suite_symbol), Card)


@pytest.mark.parametrize("suite_name", Card.SUITE_NAMES) 
@pytest.mark.parametrize("face_name", Card.FACE_NAMES) 
def test_card_using_names(face_name, suite_name):
    """Tests constructor method."""
    assert isinstance(Card(face_name, suite_name), Card)
