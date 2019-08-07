"""Blackjack Card."""

from blackjack.classes.card import Card


class BlackJackCard(Card):
    FACES = ({"name": "two", "symbol": "2", "value": (2,)},
             {"name": "three", "symbol": "3", "value": (3,)},
             {"name": "four", "symbol": "4", "value": (4,)},
             {"name": "five", "symbol": "5", "value": (5,)},
             {"name": "six", "symbol": "6", "value": (6,)},
             {"name": "seven", "symbol": "7", "value": (7,)},
             {"name": "eight", "symbol": "8", "value": (8,)},
             {"name": "nine", "symbol": "9", "value": (9,)},
             {"name": "ten", "symbol": "10", "value": (10,)},
             {"name": "jack", "symbol": "J", "value": (10,)},
             {"name": "queen", "symbol": "Q", "value": (10,)},
             {"name": "king", "symbol": "K", "value": (10,)},
             {"name": "ace", "symbol": "A", "value": (1,11)})
    FACE_VALUES = {face["symbol"]: face["value"] for face in FACES}

    def get_value(self):
        return self.FACE_VALUES[self.face]

    value = property(get_value)
