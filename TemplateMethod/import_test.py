from TemplateMethod.create_test import CreateTest


# noinspection PyMethodMayBeStatic
class ImportTest(CreateTest):

    def logic(self):
        self.import_test()
        while not self.validate_test():
            self.edit_test()
        self.upload_test()

    def import_test(self):
        print('Read the test from disk')
