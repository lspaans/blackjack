"""Dealer."""

from blackjack.classes.bank import Bank
from blackjack.classes.hand import Hand
from blackjack.classes.player import Player
from blackjack.classes.shoe import Shoe
from blackjack.exceptions.cannotsplit import CannotSplit
from blackjack.exceptions.shoeempty import ShoeEmpty
from blackjack.exceptions.handbusted import HandBusted
from blackjack.exceptions.playerbusted import PlayerBusted


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

        try: 
            if round == 1:
                if isinstance(player, Bank):
                    player.add_hand(Hand(self.shoe.deal(1)))
                else:
                    player.add_hand(Hand(self.shoe.deal(2)))

                    if player.hands[0].splittable is True:
                        player.add_hand(Hand(player.hands[0].split))
            else:
                pass
        except ShoeEmpty as exc:
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
