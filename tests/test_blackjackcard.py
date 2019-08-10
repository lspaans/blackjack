"""Tests `BlackJackCard`-class."""

import pytest

from blackjack import BlackJackCard


@pytest.mark.parametrize("suite", BlackJackCard.SUITE_SYMBOLS) 
@pytest.mark.parametrize("face", BlackJackCard.FACE_SYMBOLS) 
def test_blackjackcard(face, suite):
    """Tests constructor method with field values."""
    assert isinstance(BlackJackCard(face, suite), BlackJackCard)
