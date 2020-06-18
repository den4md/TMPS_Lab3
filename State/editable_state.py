from State.interfaces import IState


class EditableState(IState):

    def edit(self, new_content: str):
        self._content = new_content
        print(f'Content of the test has been changed to new - \'{self._content}\'')

    def view_statistics(self):
        print('Can\'t check statistics of unpublished test')
