"""Dealer."""

from blackjack.classes.bank import Bank
from blackjack.classes.player import Player
from blackjack.classes.shoe import Shoe


class Dealer(object):
    DEFAULT_NAME = "Dealer"

    def __init__(self, shoe, name=DEFAULT_NAME):
        self._name, self.name = None, name
        self._shoe, self.shoe = None, shoe

    def __repr__(self):
        return "{class_type}({name})".format(
                class_type=type(self).__name__,
                name="" if self.name == self.DEFAULT_NAME else repr(self.name)
                )

    def __str__(self):
        return self.name

    def deal(self, player, round):
        if not isinstance(player, Player):
            raise ValueError("player is of wrong type")

        if not isinstance(round, int):
            raise ValueError("round is of wrong type")

        if round == 1:
            player.cards = self.shoe.deal(1 if isinstance(player, Bank) else 2)
        else:
            pass

    def get_name(self):
        return self._name

    def get_shoe(self):
        return self._shoe

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name is of wrong type")

        self._name = name

    def set_shoe(self, shoe):
        if not isinstance(shoe, Shoe):
            raise ValueError("shoe is of wrong type")

        self._shoe = shoe

    name = property(get_name, set_name)
    shoe = property(get_shoe, set_shoe)
