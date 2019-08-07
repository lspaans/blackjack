"""Shoe."""

import random

from blackjack.classes.card import Card
from blackjack.classes.deck import Deck
from blackjack.exceptions.shoeempty import ShoeEmpty


class Shoe(object):
    DEFAULT_NAME = "Shoe"
    DEFAULT_NUMBER_OF_DECKS = 6

    def __init__(self, name=DEFAULT_NAME, decks=DEFAULT_NUMBER_OF_DECKS):
        self._cards = None
        self._name, self.name = None, name
        self._number_of_decks, self.number_of_decks = None, decks

        self._init_cards()

    def __repr__(self):
        return "{class_type}({name})".format(
                class_type=type(self).__name__,
                name="" if self.name == self._DEFAULT_NAME else repr(self.name)
                )

    def __str__(self):
        return " ".join([str(c) for c in self.cards])

    def _init_cards(self):
        self.cards = [card for _ in range(self.number_of_decks)
                      for card in Deck().cards]

    def add_card(self, card):
        if not isinstance(card, Card):
            raise ValueError("card is of wrong type")

        self._cards.append(card)

    def deal_card(self):
        return self.deal(1)[0]

    def deal(self, number):
        if not isinstance(number, int):
            raise ValueError("number is of wrong type")

        try:
            return [self.cards.pop(0) for _ in range(number)]
        except IndexError as exc:
            raise ShoeEmpty("no cards left") from exc


    def get_cards(self):
        return self._cards

    def get_name(self):
        return self._name

    def get_number_of_decks(self):
        return self._number_of_decks

    def set_cards(self, cards):
        self._cards = []

        for card in cards:
            self.add_card(card)

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name is of wrong type")

        self._name = name

    def set_number_of_decks(self, number_of_decks):
        if not isinstance(number_of_decks, int):
            raise ValueError("number of decks is of wrong type")

        self._number_of_decks = number_of_decks
        self._init_cards()

    def shuffle(self):
        random.shuffle(self.cards)

    cards = property(get_cards, set_cards)
    number_of_decks = property(get_number_of_decks, set_number_of_decks)
