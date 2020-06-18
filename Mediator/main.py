from Mediator.table import Table
from Mediator.player import Player
from Mediator.deck import Deck

if __name__ == '__main__':
    player = Player()
    deck = Deck()
    table = Table(player, deck)
    player.set_mediator(table)
    deck.set_mediator(table)

    # Game process

    deck.draw()
    deck.draw()
    deck.draw()
    player.discard()
    player.standup()
