import re

from Chain_of_Responsibility.base_player_handler import BasePlayerHandler
from Chain_of_Responsibility.player import Player


class ConcretePlayerHandler(BasePlayerHandler):

    def handle_player(self, player: Player) -> str:
        if re.match(r'\[[A-Za-z0-9.*\-_]+\]', str(player)) is not None:
            return 'game.jsp'
        else:
            return 'lobby.jsp'
