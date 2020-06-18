from Chain_of_Responsibility.iplayer_handler import IPlayerHandler
from Chain_of_Responsibility.player import Player


class BasePlayerHandler(IPlayerHandler):

    def __init__(self, next_handler: IPlayerHandler = None):
        super(BasePlayerHandler, self).__init__()
        self._next_handler = next_handler

    def handle_player(self, player: Player) -> str:
        if str(player) == '':
            return 'login.jsp'
        else:
            return self.handle_next(player)

    def handle_next(self, player: Player) -> str:
        if self._next_handler is not None:
            return self._next_handler.handle_player(player)
