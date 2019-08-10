"""Hand."""

from blackjack.classes.blackjackcard import BlackJackCard as Card
from blackjack.exceptions.handbusted import HandBusted
from blackjack.exceptions.playerbusted import PlayerBusted


class Hand(object):
    DEFAULT_NAME = "Hand"
    DEFAULT_MAXIMUM = 21

    def __init__(self, cards=None, name=DEFAULT_NAME, maximum=DEFAULT_MAXIMUM):
        if cards is None:
            cards = []

        self._maximum, self.maximum = None, maximum
        self._name, self.name = None, name
        self._cards, self.cards = None, cards

    def __repr__(self):
        return "{class_type}({arguments})".format(
                class_type=type(self).__name__,
                arguments=", ".join(["{argument}={value}".format(
                    argument=argument[1:],
                    value=repr(value)
                ) for argument, value in vars(self).items()
                        if value is not None]))

    def __str__(self):
        return " ".join([str(c) for c in self.cards])

    def add_card(self, card):
        if not isinstance(card, Card):
            raise ValueError("card is of wrong type")

        self._cards.append(card)

    def get_cards(self):
        return self._cards

    def get_highest_value(self):
        return None if len(self.values) == 0 else sorted(self.values)[-1]

    def get_lowest_value(self):
        return None if len(self.values) == 0 else sorted(self.values)[0]

    def get_maximum(self):
        return sef._maximum

    def get_name(self):
        return self._name

    def get_value(self):
        for values_number, values in enumerate([card.value for card in
                                                self.cards]):
            if values_number == 0:
                totals = list(values)
            else:
                totals = [total+value for total in totals for value in values]

        return list([total for total in set(totals) if total <= self.maximum])

    def set_cards(self, cards):
        self._cards = []

        for card in cards:
            self.add_card(card)

    def set_maximum(self, maximum):
        if not isinstance(maximum, int):
            raise ValueError("maximum is of wrong type")

        self._maximum = maximum

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name is of wrong type")

        self._name = name

    cards = property(get_cards, set_cards)
    highest_value = property(get_highest_value)
    lowest_value = property(get_lowest_value)
    maximum = property(get_maximum, set_maximum)
    name = property(get_name, set_name)
    value = property(get_value)
