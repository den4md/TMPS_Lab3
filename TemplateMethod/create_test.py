import math
from random import random


# noinspection PyMethodMayBeStatic
class CreateTest:

    def __init__(self):
        self.logic()

    def logic(self):
        self.create_test()
        self.edit_test()
        while not self.validate_test():
            self.edit_test()
        self.upload_test()

    def create_test(self):
        print("Creating empty test")

    def edit_test(self):
        print('Editing test')

    def validate_test(self) -> bool:
        result = math.floor(random()*3)
        result = bool(result)
        if result:
            print("Validated test successful")
        else:
            print("Validating of the test has failed")
        return result

    def upload_test(self):
        print("Uploaded test to the sever")
