"""Game."""

from blackjack.classes.player import Player


class Game(object):
    DEFAULT_NAME = "Game"
    DEFAULT_PLAYER_NAMES = ("Player 1", "Player 2")
    DEFAULT_PLAYER_TYPE = Player

    def __init__(self, name=DEFAULT_NAME, player_names=None):
        if player_names is None:
            player_names = self.DEFAULT_PLAYER_NAMES

        self._name, self.name = None, name
        self._players, self.players = [], player_names

    def __repr__(self):
        return "{class_type}({players})".format(
                class_type=type(self).__name__,
                players=", ".join([repr(p) for p in self.players])
                )

    def __str__(self):
        return self.name

    def add_player(self, player_name):
        if not isinstance(player_name, str):
            raise ValueError("player name is of wrong type")

        self._players.append(self.DEFAULT_PLAYER_TYPE(player_name))

    def get_name(self):
        return self._name

    def get_players(self):
        return self._players

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name is of wrong type")

        self._name = name

    def set_players(self, player_names):
        if not isinstance(player_names, (list, tuple)):
            raise ValueError("player names is of wrong type")

        for player_name in player_names:
            self.add_player(player_name)

    def start(self):
        pass

    name = property(get_name, set_name)
    players = property(get_players, set_players)
