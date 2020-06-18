from TemplateMethod.create_test import CreateTest


# noinspection PyMethodMayBeStatic
class EditTest(CreateTest):

    def create_test(self):
        self.download_test()

    def download_test(self):
        print('Downloading actual test from the server')
