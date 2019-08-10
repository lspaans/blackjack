"""Player."""

import blackjack

from blackjack.classes.card import Card
from blackjack.classes.hand import Hand


class Player(object):
    DEFAULT_NAME = "Player"

    def __init__(self, game, name=DEFAULT_NAME, hands=None):
        if hands is None:
            hands = []

        self._hands, self.hands = None, hands
        self._game, self.game = None, game
        self._name, self.name = None, name

    def __repr__(self):
        return "{class_type}({name})".format(
                class_type=type(self).__name__,
                name="" if self.name == self.DEFAULT_NAME else \
                        "name={name}".format(name=repr(self.name))
                )

    def __str__(self):
        return self.name

    def add_hand(self, hand):
        if not isinstance(hand, Hand):
            raise ValueError("hand is of wrong type")

        self._hands.append(card)

    def get_hands(self):
        return self._hands

    def get_game(self):
        return self._game

    def get_name(self):
        return self._name

    def return_hands(self):
        hands = self.hands
        self._hands = []

        return hands

    def set_hands(self, hands):
        self._hands = []

        for hand in hands:
            self.add_hand(hand)

    def set_game(self, game):
        if not isinstance(game, blackjack.BlackJack):
            raise ValueError("game is of wrong type")

        self._game = game

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name is of wrong type")

        self._name = name

    game = property(get_game, set_game)
    hands = property(get_hands, set_hands)
    name = property(get_name, set_name)
