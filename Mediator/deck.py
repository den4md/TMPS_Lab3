from Mediator.interfaces import IComponent, IMediator


class Deck(IComponent):

    def __init__(self, mediator: IMediator = None):
        super(Deck, self).__init__(mediator)
        self._cards = ['0 of yellow', '0 of red', '0 of green', '0 of blue', 'reverse of red']

    def draw(self):
        if len(self._cards) != 0:
            card = self._cards.pop()
            self._mediator.notify(self, [card])
        else:
            print('Deck has no more cards to draw')

    def add(self, cards: list):
        self._cards.extend(cards)
