from math import ceil
from random import random

from State.interfaces import IState, ITest


class PublishedState(IState):

    def __init__(self, test: ITest, state: IState = None):
        super(PublishedState, self).__init__(test, state)
        self._views = ceil(random()*1001)

    def edit(self, new_content: str):
        print('Published test can\'t be edited')

    def view_statistics(self):
        print(f'Test has been viewed {self._views} time(-s)')
