from Mediator.deck import Deck
from Mediator.interfaces import IMediator, IComponent
from Mediator.player import Player


class Table(IMediator):

    def __init__(self, player: Player, deck: Deck):
        self._player = player
        self._deck = deck

    def notify(self, sender: IComponent, cards: list):
        if isinstance(sender, Deck):
            self._player.add(cards)
        elif isinstance(sender, Player):
            self._deck.add(cards)
