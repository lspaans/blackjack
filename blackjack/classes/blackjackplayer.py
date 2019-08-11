"""BlackJackPlayer."""

from blackjack.classes.card import Card
from blackjack.classes.hand import Hand
from blackjack.classes.player import Player


class BlackJackPlayer(Player):
    # Hmmm.
    DEFAULT_GAME_TYPE = object
    DEFAULT_NAME = "Player"

    def __init__(self, game, name=DEFAULT_NAME, hands=None):
        super().__init__(game, name=name)

        if hands is None:
            hands = []

        self._hands, self.hands = None, hands

    def add_hand(self, hand):
        if not isinstance(hand, Hand):
            raise ValueError("hand is of wrong type")

        self._hands.append(hand)

    @staticmethod
    def _draws(player_hand, bank_hand):
        pass

    @staticmethod
    def _splits(player_hand, bank_hand):
        pass

    @staticmethod
    def _stands(player_hand, bank_hand):
        pass

    def get_action(self, player_hand, bank_hand):
        if self._draws(player_hand, bank_hand) is True:
            return "draw"
        elif self._splits(player_hand, bank_hand) is True:
            return "split"
        elif self._stands(player_hand, bankd_hand) is True:
            return "stand"
        else:
            # Introduce `UndecidedAction` here?
            raise ValueError("unknown action error")

    def get_hands(self):
        return self._hands

    def get_number_of_hands(self):
        return len(self.hands)

    def return_hands(self):
        hands = self.hands
        self._hands = []

        return hands

    def set_hands(self, hands):
        self._hands = []

        for hand in hands:
            self.add_hand(hand)

    hands = property(get_hands, set_hands)
    number_of_hands = property(get_number_of_hands)
