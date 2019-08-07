"""Card."""


class Card(object):
    FACES = ({"name": "two", "symbol": "2"},
             {"name": "three", "symbol": "3"},
             {"name": "four", "symbol": "4"},
             {"name": "five", "symbol": "5"},
             {"name": "six", "symbol": "6"},
             {"name": "seven", "symbol": "7"},
             {"name": "eight", "symbol": "8"},
             {"name": "nine", "symbol": "9"},
             {"name": "ten", "symbol": "10"},
             {"name": "jack", "symbol": "J"},
             {"name": "queen", "symbol": "Q"},
             {"name": "king", "symbol": "K"},
             {"name": "ace", "symbol": "A"})
    SUITES = ({"name": "clubs", "symbol": "C"},
              {"name": "diamonds", "symbol": "D"},
              {"name": "hearts", "symbol": "H"},
              {"name": "spades", "symbol": "S"})
    FACE_NAMES = [face["name"] for face in FACES]
    FACE_SYMBOLS = [face["symbol"] for face in FACES]
    SUITE_NAMES = [suite["name"] for suite in SUITES]
    SUITE_SYMBOLS = [suite["symbol"] for suite in SUITES]

    def __init__(self, face, suite):
        self._face_symbol, self.face = None, face
        self._suite_symbol, self.suite = None, suite

    def __repr__(self):
        return "{class_type}({face}, {suite})".format(
                class_type=type(self).__name__, face=repr(self.face),
                suite=repr(self.suite))

    def __str__(self):
        return "{face_symbol}{suite_symbol}".format(
                face_symbol=self.face_symbol, suite_symbol=self.suite_symbol)

    @classmethod
    def from_name(cls, name):
        if not isinstance(name, str):
            raise ValueError("unknown card name type")

        if len(name) < 2:
            raise ValueError("unrecognized card name")

        return cls(name[0:-1], name[-1])

    def get_display_name(self):
        return "{face_name} of {suite_name}".format(
                face_name=self.face_name.capitalize(),
                suite_name=self.suite_name.capitalize())

    def get_face(self):
        return self.face_symbol

    def get_face_name(self):
        return self._face_name

    def get_face_symbol(self):
        return self._face_symbol

    def get_suite(self):
        return self.suite_symbol

    def get_suite_name(self):
        return self._suite_name

    def get_suite_symbol(self):
        return self._suite_symbol

    def set_face(self, face_reference):
        for face in self.FACES:
            if face_reference not in (face["name"], face["symbol"]):
                continue

            self._face_name = face["name"]
            self._face_symbol = face["symbol"]

            break
        else:
            raise ValueError(
                    "unknown face reference: \"{face_reference}\"".format(
                        face_reference=face_reference))

    def set_face_name(self, face_name):
        if face_name not in self.FACE_NAMES:
            raise ValueError("unknown face name: \"{face_name}\"".format(
                face_name=face_name))

        self.face = face_name

    def set_face_symbol(self, face_symbol):
        if face_symbol not in self.FACE_SYMBOLS:
            raise ValueError("unknown face symbol: \"{face_symbol}\"".format(
                face_symbol=face_symbol))

        self.face = face_symbol

    def set_suite(self, suite_reference):
        for suite in self.SUITES:
            if suite_reference not in (suite["name"], suite["symbol"]):
                continue

            self._suite_name = suite["name"]
            self._suite_symbol = suite["symbol"]

            break
        else:
            raise ValueError(
                    "unknown suite reference: \"{suite_reference}\"".format(
                        suite_reference=suite_reference))

    def set_suite_name(self, suite_name):
        if suite_name not in self.SUITE_NAMES:
            raise ValueError("unknown suite name: \"{suite_name}\"".format(
                suite_name=suite_name))

        self.suite = suite_name

    def set_suite_symbol(self, suite_symbol):
        if suite_symbol not in self.SUITE_SYMBOLS:
            raise ValueError("unknown suite symbol: \"{suite_symbol}\"".format(
                suite_symbol=suite_symbol))

        self.suite = suite_symbol

    display_name = property(get_display_name)
    face = property(get_face, set_face)
    face_name = property(get_face_name, set_face_name)
    face_symbol = property(get_face_symbol, set_face_symbol)
    suite = property(get_suite, set_suite)
    suite_name = property(get_suite_name, set_suite_name)
    suite_symbol = property(get_suite_symbol, set_suite_symbol)
