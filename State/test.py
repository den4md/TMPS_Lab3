from State.editable_state import EditableState
from State.interfaces import ITest, IState
from State.published_state import PublishedState


class Test(ITest):

    def publish(self):
        if isinstance(self._state, EditableState):
            self.change_state(PublishedState)
            print('Test is published successful')
        else:
            print('Test is already published')

    def change_state(self, state_class):
        if issubclass(state_class, IState):
            self._state = state_class(self, self._state)

    def __init__(self):
        self._state = EditableState(self)
        print('Test has been created')

    def edit(self, new_content):
        self._state.edit(new_content)

    def view_statistics(self):
        self._state.view_statistics()


