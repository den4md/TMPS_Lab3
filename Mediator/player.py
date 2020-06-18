from Mediator.interfaces import IComponent, IMediator


class Player(IComponent):

    def __init__(self, mediator: IMediator = None):
        super(Player, self).__init__(mediator)
        self._cards = []

    def discard(self):
        if len(self._cards) != 0:
            card = self._cards.pop()
            print(f'Player has discarded card - {card}')
            self._mediator.notify(self, [card])

    def standup(self):
        card_ref = list(self._cards)
        self._cards = []
        print(f'Player has exitted the table and discarded these cards to the deck - {card_ref}')
        self._mediator.notify(self, card_ref)

    def add(self, cards: list):
        self._cards.extend(cards)
        print(f'Player has drew these cards - {cards}')
