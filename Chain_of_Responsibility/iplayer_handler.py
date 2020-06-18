from __future__ import annotations
from abc import ABC, abstractmethod

from Chain_of_Responsibility.player import Player


class IPlayerHandler(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def handle_player(self, player: Player) -> str:
        pass

    @abstractmethod
    def handle_next(self, player: Player) -> str:
        pass
