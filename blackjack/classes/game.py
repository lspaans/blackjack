"""Game."""

import logging

from blackjack.classes.player import Player


class Game(object):
    _PLAYER_TYPE = Player

    DEFAULT_NAME = "Game"
    DEFAULT_NUMBER_OF_PLAYERS = 0
    DEFAULT_PLAYER_NAME_TEMPLATE = "Player {num}"

    def __init__(self, logger_name=__name__, name=DEFAULT_NAME,
                 players=DEFAULT_NUMBER_OF_PLAYERS,
                 player_name_template=DEFAULT_PLAYER_NAME_TEMPLATE):
        self._logger, self.logger = None, logging.getLogger(logger_name)
        self._name, self.name = None, name
        self._players, self.players = [], [self._PLAYER_TYPE(self,
                name=player_name_template.format(num=num+1))
                        for num in range(players)]

    def __repr__(self):
        return "{class_type}({players})".format(
                class_type=type(self).__name__,
                players=", ".join([repr(p) for p in self.players])
                )

    def __str__(self):
        return self.name

    def add_player(self, player):
        if not isinstance(player, self._PLAYER_TYPE):
            raise ValueError("player is of wrong type")

        self._players.append(player)

    def get_logger(self):
        return self._logger

    def get_name(self):
        return self._name

    def get_number_of_players(self):
        return len(self.players)

    def get_player_type(self):
        return self._player_type

    def get_players(self):
        return self._players

    def set_logger(self, logger):
        if not isinstance(logger, logging.Logger):
            raise ValueError("logger is of wrong type")

        self._logger = logger

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name is of wrong type")

        self._name = name

    def set_players(self, players):
        if not isinstance(players, (list, tuple)):
            raise ValueError("players is of wrong type")

        for player in players:
            self.add_player(player)

    def start(self):
        self.logger.info("{name} started.".format(name=self.name))

    logger = property(get_logger, set_logger)
    name = property(get_name, set_name)
    number_of_players = property(get_number_of_players)
    players = property(get_players, set_players)
