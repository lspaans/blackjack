"""Player."""


class Player(object):
    # Hmmm.
    DEFAULT_GAME_TYPE = object
    DEFAULT_NAME = "Player"

    def __init__(self, game, name=DEFAULT_NAME):
        self._game, self.game = None, game
        self._name, self.name = None, name

    def __repr__(self):
        return "{class_type}({game}, {name})".format(
                class_type=type(self).__name__,
                game=repr(game),
                name="" if self.name == self.DEFAULT_NAME else \
                        "name={name}".format(name=repr(self.name))
                )

    def __str__(self):
        return self.name

    def get_game(self):
        return self._game

    def get_name(self):
        return self._name

    def set_game(self, game):
        if not isinstance(game, self.DEFAULT_GAME_TYPE):
            raise ValueError("game is of wrong type")

        self._game = game

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name is of wrong type")

        self._name = name

    game = property(get_game, set_game)
    name = property(get_name, set_name)
