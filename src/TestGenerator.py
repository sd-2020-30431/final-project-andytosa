
class Test:
    def __init__(self, name):
        self.name = name
        self.testItems = []
        self.variables = {}

    def addTestItem(self, testItem):
        self.testItems.append(testItem)

    def generate(self):
        res = ""
        for ti in self.testItems:
            res += ti.generate()

        return res


class TestGenerator:
    def __init__(self, test_obj):
        self.test_obj = test_obj

    def generate(self, number):
        for i in range(number):
            f = open("tests/{self.test_obj.getName()}{i}.in", "w")
            f.write(self.test_obj.generate())
            f.close()

