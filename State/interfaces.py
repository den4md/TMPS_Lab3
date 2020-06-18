from __future__ import annotations
from abc import ABC, abstractmethod


class ITest(ABC):

    @abstractmethod
    def publish(self):
        pass

    @abstractmethod
    def change_state(self, state: IState):
        pass


class IState(ABC):

    def __init__(self, test: ITest, state: IState = None):
        if state is None:
            self._content = ''
        else:
            self._content = state._content
        self.test = test
        if hasattr(state, '_views'):
            print('Views has been reset')

    @abstractmethod
    def edit(self, new_content: str):
        pass

    @abstractmethod
    def view_statistics(self):
        pass
