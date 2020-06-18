from Chain_of_Responsibility.base_player_handler import BasePlayerHandler
from Chain_of_Responsibility.concrete_player_handler import ConcretePlayerHandler
from Chain_of_Responsibility.iplayer_handler import IPlayerHandler
from Chain_of_Responsibility.player import Player


def client(player: Player, player_handler: IPlayerHandler):
    dict_of_views = {
        'login.jsp': lambda: print('Returning view LOGIN'),
        'game.jsp': lambda: print('Returning view GAME'),
        'lobby.jsp': lambda: print('Returning view LOBBY'),
        None: lambda: print('Returning view ERROR')
    }
    dict_of_views[player_handler.handle_player(player)]()


if __name__ == '__main__':
    full_player_handler = BasePlayerHandler(ConcretePlayerHandler())

    client(Player(''), full_player_handler)
    client(Player('[Ivan]'), full_player_handler)
    client(Player('---007---'), full_player_handler)
    client(Player('---007---'), BasePlayerHandler())
