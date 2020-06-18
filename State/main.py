from State.editable_state import EditableState
from State.test import Test

if __name__ == '__main__':
    test = Test()
    test.publish()
    test.view_statistics()
    test.edit('Py')
    test.change_state(EditableState)
    test.edit('Py')
    test.view_statistics()
    test.publish()
    test.view_statistics()
