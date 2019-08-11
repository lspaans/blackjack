"""Tests `Card`-class."""

import pytest

from blackjack import BlackJackCard


@pytest.mark.parametrize("suite_symbol", BlackJackCard.SUITE_SYMBOLS) 
@pytest.mark.parametrize("face_symbol", BlackJackCard.FACE_SYMBOLS) 
def test_blackjackcard_using_symbols(face_symbol, suite_symbol):
    """Tests constructor method."""
    assert isinstance(BlackJackCard(face_symbol, suite_symbol), BlackJackCard)


@pytest.mark.parametrize("suite_name", BlackJackCard.SUITE_NAMES) 
@pytest.mark.parametrize("face_name", BlackJackCard.FACE_NAMES) 
def test_blackjackcard_using_names(face_name, suite_name):
    """Tests constructor method."""
    assert isinstance(BlackJackCard(face_name, suite_name), BlackJackCard)
