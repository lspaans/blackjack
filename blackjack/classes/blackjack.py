"""Game."""

from blackjack.classes.bank import Bank
from blackjack.classes.dealer import Dealer
from blackjack.classes.game import Game
from blackjack.classes.blackjackplayer import BlackJackPlayer
from blackjack.classes.shoe import Shoe


class BlackJack(Game):
    _PLAYER_TYPE = BlackJackPlayer

    DEFAULT_BANK_NAME = "Bank Player"
    DEFAULT_DEALER_NAME = "Dealer"
    DEFAULT_NAME = "BlackJack"
    DEFAULT_NUMBER_OF_PLAYERS = 1
    DEFAULT_PLAYER_NAME_TEMPLATE = "Player {num}"
    DEFAULT_SHOE_NAME = "Shoe"

    def __init__(self, bank_name=DEFAULT_BANK_NAME,
                 dealer_name=DEFAULT_DEALER_NAME, name=DEFAULT_NAME,
                 player_name_template=DEFAULT_PLAYER_NAME_TEMPLATE,
                 players=DEFAULT_NUMBER_OF_PLAYERS,
                 shoe_name=DEFAULT_SHOE_NAME):
        super().__init__(name=name, players=players,
                         player_name_template=player_name_template)
        self._bank, self.bank = None, Bank(self, name=bank_name)
        self._shoe, self.shoe = None, Shoe(name=shoe_name)
        self._dealer, self.dealer = None, Dealer(self.shoe, name=dealer_name)
        self._round, self.round = None, 0

    def get_bank(self):
        return self._bank

    def get_dealer(self):
        return self._dealer

    def get_round(self):
        return self._round

    def get_shoe(self):
        return self._shoe

    def next_round(self):
        self.round += 1

    def set_bank(self, bank):
        if not isinstance(bank, Bank):
            raise ValueError("bank is of wrong type")

        self._bank = bank

    def set_dealer(self, dealer):
        if not isinstance(dealer, Dealer):
            raise ValueError("dealer is of wrong type")

        self._dealer = dealer

    def set_round(self, round):
        if not isinstance(round, int):
            raise ValueError("round is of wrong type")

        self._round = round

    def set_shoe(self, shoe):
        if not isinstance(shoe, Shoe):
            raise ValueError("shoe is of wrong type")

        self._shoe = shoe
        self.shoe.shuffle()

    def start(self):
        super().start()

        while True:
            self.next_round()
            for player in self.players:
                self.dealer.deal(player, self.round)
            print(self.round)

    bank = property(get_bank, set_bank)
    dealer = property(get_dealer, set_dealer)
    round = property(get_round, set_round)
    shoe = property(get_shoe, set_shoe)
