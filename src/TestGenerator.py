import os

class Test:
    def __init__(self, name):
        self.name = name
        self.testItems = []
        self.variables = {}

    def getName(self):
        return self.name

    def addItem(self, testItem):
        self.testItems.append(testItem)

    def generate(self):
        res = ""
        for ti in self.testItems:
            res += ti.generate()

        return res


class TestGenerator:
    def __init__(self, test_obj, dir_name = "tests"):
        self.test_obj = test_obj
        self.dir_name = dir_name

    def generate(self, number):
        if not os.path.exists(self.dir_name):
            os.makedirs(self.dir_name)

        for i in range(number):
            f = open(f"tests/{self.test_obj.getName()}{i}.in", "w")
            f.write(self.test_obj.generate())
            f.close()

