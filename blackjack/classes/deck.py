"""Deck."""

import random

from blackjack.classes.blackjackcard import BlackJackCard as Card


class Deck(object):
    DEFAULT_NAME = "Deck"
    SUITE_SYMBOLS = Card.SUITE_SYMBOLS
    FACE_SYMBOLS = Card.FACE_SYMBOLS

    def __init__(self, name=DEFAULT_NAME):
        self._name, self.name = None, name
        self._cards = None

        self._init_cards()

    def __repr__(self):
        return "{class_type}({name})".format(
                class_type=type(self).__name__,
                name="" if self.name == self.DEFAULT_NAME else repr(self.name)
                )

    def __str__(self):
        return " ".join([str(c) for c in self.cards])

    def _init_cards(self):
        self.cards = [Card(face, suite) for suite in self.SUITE_SYMBOLS
                      for face in self.FACE_SYMBOLS]

    def add_card(self, card):
        if not isinstance(card, Card):
            raise ValueError("card is of wrong type")

        self._cards.append(card)

    def get_cards(self):
        return self._cards

    def get_name(self):
        return self._name

    def set_cards(self, cards):
        self._cards = []

        for card in cards:
            self.add_card(card)

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name is of wrong type")

        self._name = name

    def shuffle(self):
        random.shuffle(self.cards)

    cards = property(get_cards, set_cards)
    name = property(get_name, set_name)
