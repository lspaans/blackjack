"""Game."""

from blackjack.classes.bank import Bank
from blackjack.classes.dealer import Dealer
from blackjack.classes.game import Game
from blackjack.classes.player import Player
from blackjack.classes.shoe import Shoe


class BlackJack(Game):
    DEFAULT_BANK_NAME = "Bank Player"
    DEFAULT_DEALER_NAME = "Dealer"
    DEFAULT_NAME = "BlackJack"
    DEFAULT_NUMBER_OF_PLAYERS = 1
    DEFAULT_PLAYER_NAME = "Player {num}"
    DEFAULT_SHOE_NAME = "Shoe"

    def __init__(self, bank_name=DEFAULT_BANK_NAME,
                 dealer_name=DEFAULT_DEALER_NAME, name=DEFAULT_NAME,
                 players=DEFAULT_NUMBER_OF_PLAYERS,
                 shoe_name=DEFAULT_SHOE_NAME):
        self._bank, self.bank = None, Bank(self, name=bank_name)
        self._name, self.name = None, name
        self._number_of_players, self.number_of_players = None, players
        self._players = None
        self._round, self.round = None, 0
        self._shoe, self.shoe = None, Shoe(name=shoe_name)

        self._init_dealer(name=dealer_name)
        self._init_players()

    def _init_dealer(self, name):
        self.dealer = Dealer(self.shoe, name=name)

    def _init_players(self):
        self.players = [Player(self, name=self.DEFAULT_PLAYER_NAME.format(
            num=num+1)) for num in range(self.number_of_players)]

    def add_player(self, player):
        if not isinstance(player, Player):
            raise ValueError("player is of wrong type")

        self.players.append(player)

    def get_bank(self):
        return self._bank

    def get_dealer(self):
        return self._dealer

    def get_name(self):
        return self._name

    def get_number_of_players(self):
        return self._number_of_players

    def get_players(self):
        return self._players

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

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name is of wrong type")

        self._name = name

    def set_number_of_players(self, number_of_players):
        if not isinstance(number_of_players, int):
            raise ValueError("number of players is of wrong type")

        self._number_of_players = number_of_players

    def set_players(self, players):
        if not isinstance(players, (list, tuple)):
            raise ValueError("players is of wrong type")

        self._players = [self.bank]

        for player in players:
            self.add_player(player)

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
    name = property(get_name, set_name)
    number_of_players = property(get_number_of_players, set_number_of_players)
    players = property(get_players, set_players)
    round = property(get_round, set_round)
    shoe = property(get_shoe, set_shoe)
