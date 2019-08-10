"""Tests `BlackJackPlayer`-class."""

import pytest

from blackjack import BlackJackPlayer


def test_blackjackplayer(example_blackjack):
    """Tests constructor method."""
    assert isinstance(BlackJackPlayer(example_blackjack), BlackJackPlayer)
