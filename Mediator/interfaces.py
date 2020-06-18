from __future__ import annotations
from abc import ABC, abstractmethod


class IMediator(ABC):

    @abstractmethod
    def notify(self, sender: IComponent, cards: list):
        pass


# noinspection PyAttributeOutsideInit,PyTypeChecker
class IComponent(ABC):

    def __init__(self, mediator: IMediator = None):
        self.set_mediator(mediator)

    def set_mediator(self, mediator: IMediator):
        self._mediator = mediator

    def clear_mediator(self):
        self.set_mediator(None)
