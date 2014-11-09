#!/usr/bin/env python

import random
import time

class BlackJackObject(object):

    def isValidType(self, objectType, validType):
        return(isinstance(objectType, validType))

class Card(BlackJackObject):

    faces = (
        '2', '3', '4',  '5', '6',
        '7', '8', '9', '10',
        'J', 'Q', 'K',  'A'
    )
    suits = ('C', 'D', 'H', 'S')
    states = ('blind', 'visible')

    def __init__(self, face, suite, state='blind'):
        self.setType(face, suite)
        self.setState(state)

    def setType(self, face, suite):
        if (
            self.isValidType(suite, str) and
            suite.upper() in self.getSuits()
        ):
            self.suite = suite
        else:
            raise Exception(
                "Invalid suite: '{0}'".format(suite)
            )
        if (
            self.isValidType(face, str) and
            face.upper() in self.getFaces()
        ):
            self.face = face 
        else:
            raise Exception(
                "Invalid face: '{0}'".format(face)
            )

    def setState(self, state):
        if state in self.getStates():
            self.state = state
        else:
            raise Exception(
                "Invalid state: '{0}'".format(state)
            )

    def getState(self):
        return(self.state)

    def isBlind(self):
        return(self.getState() == 'blind')

    def isVisible(self):
        return(self.getState() == 'visible')

    def getType(self):
        return("{0}{1}".format(self.face, self.suite))

    def getFaces(self):
        return(self.faces)

    def getSuits(self):
        return(self.suits)

    def getStates(self):
        return(self.states)

    def __str__(self):
        if self.isVisible():
            return(self.getType())
        else:
            return('XX')

class BlackJackCard(Card):

    valueMap = {
        '2':  (2,), '3':  (3,),  '4':  (4,),
        '5':  (5,), '6':  (6,),  '7':  (7,),
        '8':  (8,), '9':  (9,), '10': (10,),
        'J': (10,), 'Q': (10,),  'K': (10,),  'A': (1,11)
    }
    faces = valueMap.keys()
    suits = ('C', 'D', 'H', 'S')

    def __init__(self, face, suite, state='blind'):
        super(BlackJackCard, self).__init__(
            face, suite, state
        )
        self.setValue(self.valueMap[face])

    def setValue(self, values):
        if (
            self.isValidType(values, tuple) and
            not len(
                filter(
                    lambda value:
                    not self.isValidType(value, int),
                    values
                )
            )
        ):
            self.values = values
        else:
            raise Exception(
                "Invalid value-list: '{0}'".format(
                    repr(values)
                )
            )

    def getValue(self):
        return(self.values)

class CardSet(BlackJackObject):

    CardClass = Card

    def __init__(self, cards=[]):
        self.setCards(cards)

    def setCards(self, cards=[]):
        self.cards = []
        for card in cards:
            self.addCard(card)

    def getCards(self):
        return(self.cards)

    def addCard(self, card):
        if self.isValidType(card, self.CardClass):
            self.cards.append(card)
        else:
            raise Exception(
                "Invalid card-type: '{0}'".format(
                    type(card)
                )
            )

    def shuffle(self):
        random.shuffle(self.getCards())

    def __str__(self):
        lines = ""
        for n, card in enumerate(self.getCards()):
            if n > 0 and n % 8 == 0:
                 lines += "\n"
            lines += "{0:3s} ".format(card)
        return(lines)

class BlackJackCardSet(CardSet):

    CardClass = BlackJackCard

    def getValue(self):

        # HIERO: Hier moet ik nog correct omgaan met 'blind' cards

        def multiAdd(n, m):
            a = set()
            for i in n:
                for j in m:
                    a.add(i+j)
            return(list(a))

        value = (0,)
        for card in map(
            lambda card: card, self.getCards()
        ):
            if card.isVisible():
                value = multiAdd(value, card.getValue())
        return(value)

    def getValueType(self, type):
        if len(self.getValue()) > 0:
            m = filter(lambda v: v <= 21, sorted(self.getValue()))
            if len(m) > 0:
                if type == 'high':
                    return(max(m))
                elif type == 'low':
                    return(min(m))
                else:
                    return(None)
            else:
                return(None)
        else:
            return(0)

    def getHighestValue(self):
        return(self.getValueType('high'))

    def getLowestValue(self):
        return(self.getValueType('low'))

class CardGameHand(CardSet):

    def returnCards(self):
        cards = self.cards
        self.setCards()
        return(cards)

class BlackJackHand(BlackJackCardSet, CardGameHand):

    validStates = (
        'folded', 'busted', 'playing', 'waiting'
    )

    def __init__(self):
        super(BlackJackHand, self).__init__()

    def getState(self):
        return(self.state)

    def resetState(self):
        self.setState('waiting')

    def setState(self, state):
        if state in self.validStates:
            self.state = state
            print(
                "Hand state: '{0}'".format(
                    self.getState()
                )
            )
        else:
            raise Exception(
                "Invalid state: '{0}'".format(state)
            )

class CardGameHandSet(BlackJackObject):

    HandClass = CardGameHand

    def __init__(self, hands=None):
        self.setHands(hands)

    def setHands(self, hands=None):
        self.hands = []
        if not hands:
            hands = [self.HandClass()]
        if self.isValidType(hands, list):
            for hand in hands:
                self.addHand(hand)
        else:
            raise Exception(
                "Invalid hands-type: '{0}'".format(
                    type(repr(hands))
                )
            )

    def getHands(self):
        return(self.hands)

    def addHand(self, hand):
        if self.isValidType(hand, self.HandClass):
            self.hands.append(hand)
        else:
            raise Exception(
                "Invalid hand-type: '{0}'".format(
                    type(hand)
                )
            )

    def returnHands(self):
        hands = self.hands
        self.setHands()
        return(hands)

class BlackJackHandSet(CardGameHandSet):

    HandClass = BlackJackHand

    def __init__(self):
        super(BlackJackHandSet, self).__init__()

class CardGameDeck(CardSet):

    CardClass = Card

    def __init__(self):
       super(CardGameDeck,  self).__init__()
       self.initCards()

    def initCards(self, cards=None):
        if cards is None:
            for suit in self.CardClass.suits:
                for face in self.CardClass.faces:
                    self.addCard(
                        self.CardClass(face, suit)
                    )
        else:
            for card in cards:
                self.addCard(card)

    def addCard(self, card):
        card.setState('blind')
        super(CardGameDeck, self).addCard(card)

class BlackJackDeck(BlackJackCardSet, CardGameDeck):

    CardClass = BlackJackCard

class CardGameShoe(CardSet):

    DeckClass = CardGameDeck

    def __init__(self, numberOfDecks):
        self.setCards(numberOfDecks)

    def addCard(self, card):
        card.setState('blind')
        super(CardGameShoe, self).addCard(card)

    def setCards(self, numberOfDecks):
        self.cards = []
        for n in xrange(numberOfDecks):
            deck = self.DeckClass()
            for card in deck.getCards():
                self.getCards().append(card)

    def getCards(self):
        return(self.cards)

    def dealCard(self, state=None):
        card = self.getCards().pop(0)
        if not state is None:
            card.setState(state)
        return(card)

    def shuffle(self):
        random.shuffle(self.getCards())

    def __str__(self):
        lines = ""
        for n, card in enumerate(self.getCards()):
            if n > 0 and n % 8 == 0:
                 lines += "\n"
            lines += "{0:3s} ".format(str(card))
        return(lines)

class BlackJackShoe(CardGameShoe, BlackJackCardSet):

    DeckClass = BlackJackDeck
    numberOfDecks = 5

    def __init__(self):
        super(BlackJackShoe, self).__init__(
            self.numberOfDecks
        )

class CardGamePlayer(BlackJackObject):

    HandSetClass = CardGameHandSet

    validStates = (
        'resigned', 'busted', 'playing', 'waiting'
    )

    def __init__(self, name="Player", cash=0.0):
        self.setName(name)
        self.setCash(cash)
        self.setState('waiting')
        self.setHandSet(self.HandSetClass())

    def setName(self, name):
        if self.isValidType(name, str) and len(name) > 0:
            self.name = name
        else:
            raise Exception(
                "Invalid name: '{0}'".format(name)
            )

    def getName(self):
        return(self.name)

    def setCash(self, cash):
        if (
            self.isValidType(cash, float) or
            self.isValidType(cash, int)
        ):
            self.cash = float(cash)
        else:
            raise Exception(
                "Invalid cash-type: '{0}'".format(type(cash))
            )

    def getCash(self):
        return(self.cash)

    def resetState(self):
        self.setState('waiting')

    def setState(self, state):
        if state in self.validStates:
            self.state = state
            print(
                "Player {0} state: '{1}'".format(
                    self.name, self.getState()
                )
            )
        else:
            raise Exception(
                "Invalid state: '{0}'".format(state)
            )

    def getState(self):
        return(self.state)

    def setHandSet(self, handset):
        if self.isValidType(handset, self.HandSetClass):
            self.handset = handset
        else:
            raise Exception(
                (
                    "Invalid handset-type: '{0}'"
                ).format(type(handset))
            )

    def getHandSet(self):
        return(self.handset)

    def getHands(self):
        return(self.getHandSet().getHands())

class BlackJackPlayer(CardGamePlayer):

    HandSetClass = BlackJackHandSet

    def __init__(self, name="Player", cash=0.0):
        super(BlackJackPlayer, self).__init__(name, cash)

    def play(self, shoe, bank):
        self.setState('playing')
        for n, hand in enumerate(self.getHands()):
            while hand.getHighestValue() < 15:
                time.sleep(int(5*random.random()))
                hand.addCard(shoe.dealCard('visible'))
                print((
                    "player {0} has {1} (hand={2}," + 
                    "value='{3}')"
                ).format(
                    self.getName(),
                    hand, n,
                    hand.getHighestValue()
                ))
            if hand.getHighestValue() > 21:
                hand.setState('busted')
            else:
                hand.setState('folded')

class BlackJackBank(BlackJackPlayer):

    validStates = (
        'folded', 'busted', 'playing', 'waiting'
    )

    def __init__(self, name="Bank", cash=10000000.0):
        super(BlackJackBank, self).__init__(name, cash)

    def play(self, shoe):
        self.setState('playing')
        for n, hand in enumerate(self.getHands()):
            for card in hand.getCards():
                card.setState('visible')
            while hand.getHighestValue() <= 16:
                time.sleep(int(5*random.random()))
                hand.addCard(shoe.dealCard('visible'))
                print((
                    "player {0} has {1} (hand='{2},value='{3}')"
                ).format(
                    self.getName(),
                    hand, n,
                    hand.getHighestValue()
                ))
                if hand.getHighestValue() > 21:
                    self.setState('busted')
                else:
                   self.setState('folded')

class CardGameController(BlackJackObject):

    PlayerClass = CardGamePlayer

    def __init__(self, players):
        self.setPlayers(players)
        self.setRound(0)

    def setPlayers(self, players):
        if (
            self.isValidType(players, list) and
            not len(
                filter(
                    lambda player:
                    not self.isValidType(player, self.PlayerClass),
                    players
                )
            )
        ):
            self.players = players
        else:
            raise Exception(
                (
                    "Invalid player-list: '{0}'"
                ).format(repr(players))
            )

    def getPlayers(self):
        return(self.players)

    def setRound(self, round):
        if self.isValidType(round, int):
            self.round = round
        else:
            raise Exception(
                (
                    "Invalid round-type: '{0}'"
                ).format(type(round))
            )

    def getRound(self):
        return(self.round)

    def hasPlayersWithState(self, state):
        for player in self.getPlayers():
            if player.getState() == state:
                return True
        return False

    def hasFoldedPlayers(self):
        return(self.hasPlayersWithState('folded'))

    def processResignedPlayers(self):
        self.setPlayers(
            filter(
                lambda player:
                player.getState() != 'resigned',
                self.getPlayers()
            )
        )

    def resetStatePlayers(self):
        for player in self.getPlayers():
            player.resetState()

    def update(self):
        self.processResignedPlayers()
        self.resetStatePlayers()

class BlackJackController(CardGameController):

    PlayerClass = BlackJackPlayer

    def __init__(self, players, bank, shoe):
        super(BlackJackController, self).__init__(players)
        self.setBank(bank)
        self.setShoe(shoe)

    def setBank(self, bank):
        if self.isValidType(bank, BlackJackBank):
            self.bank = bank
        else:
            raise Exception(
                (
                    "Invalid bank-type: '{0}'"
                ).format(type(bank))
            )

    def getBank(self):
        return(self.bank)

    def setShoe(self, shoe):
        if self.isValidType(shoe, BlackJackShoe):
            self.shoe = shoe
            self.getShoe().shuffle()
        else:
            raise Exception(
                (
                    "Invalid shoe-type: '{0}'"
                ).format(type(shoe))
            )

    def getShoe(self):
        return(self.shoe)

    def doTurn(self):
        while len(self.getPlayers()) > 0:
            self.initRound()

            for player in self.getPlayers():
                for n, hand in enumerate(player.getHands()):
                    print((
                        "player {0} has {1} ({2})"
                    ).format(
                        player.getName(),
                        hand, n
                    ))
                # HIERO: Moet ik de speler laten spelen. En dan een extra parameter 'hand' meegeven,
                # of moet ik een Hand() laten spelen?
                player.play(
                    self.getShoe(),
                    self.getBank()
                )
                yield(player)

            if self.hasFoldedPlayers():
                for n, hand in enumerate(self.getBank().getHands()):
                    print((
                        "player {0} has {1} ({2})"
                    ).format(
                        self.getBank().getName(),
                        hand, n
                    ))
                self.getBank().play(self.getShoe())
                yield(self.getBank())

            self.update()

    def initRound(self):
        self.increaseRound()
        self.collectCards()
        self.dealCards()

    def increaseRound(self):
        self.setRound(self.getRound()+1)

    def collectCards(self):
        for player in self.getPlayers():
            self.collectPlayerCards(player)
        self.collectPlayerCards(self.getBank())

    def collectPlayerCards(self, player):
        for hand in player.getHands():
            for card in hand.returnCards():
                self.shoe.addCard(card)

    def dealCards(self):
        for player in self.getPlayers():
            self.dealPlayerCards(player)
        self.dealPlayerCards(self.getBank())

    def dealPlayerCards(self, player):
        for state in ('visible', 'blind'):
            for hand in player.getHands():
                hand.addCard(
                    self.shoe.dealCard('visible')
                )

    def update(self):
        super(BlackJackController, self).update()
        self.getBank().resetState()

class CardGame(BlackJackObject):

    ControllerClass = BlackJackController
    PlayerClass = CardGamePlayer

    def __init__(self, numberOfPlayers):
        self.setController(
            self.ControllerClass(
                map(
                    lambda n: self.PlayerClass(
                        "Player{0}".format(n+1)
                    ), xrange(numberOfPlayers)
                )
            )
        )

    def setController(self, controller):
        if self.isValidType(controller, self.ControllerClass):
            self.controller = controller
        else:
            raise Exception(
                (
                    "Invalid controller-type: '{0}'"
                ).format(type(controller))
            )

    def getController(self):
        return(self.controller)

    def start(self):
        try:
            for player in self.getController().doTurn():
                pass
        except KeyboardInterrupt:
            pass

class BlackJack(CardGame):

    ControllerClass = BlackJackController
    PlayerClass = BlackJackPlayer
    BankClass = BlackJackBank
    ShoeClass = BlackJackShoe

    def __init__(self, numberOfPlayers=1, cash=100.0):
        super(CardGame, self).__init__()
        self.setController(
            self.ControllerClass(
                map(
                    lambda n: self.PlayerClass(
                        "Player{0}".format(n+1),
                        cash
                    ), xrange(numberOfPlayers)
                ),
                self.BankClass(),
                self.ShoeClass()
            )
        )

if __name__ == '__main__':
    game = BlackJack(1)
    game.start()
