import random


class TestItem:
    def generate(self):
        pass
    def __str__(self):
        pass



class RepeatContainer(TestItem):
    def __init__(self, name, var):
        self.var = var
        self.name = name
        self.testItems = []

    def addItem(self, testItem):
        self.testItems.append(testItem)
    
    def getName(self):
        return self.name

    def generate(self):
        res = ""
        for _ in range(self.var.getValue()):
            for ti in self.testItems:
                res += ti.generate()

        return res

    def __str__(self):
        res = f"Repeat (self.name):\n"
        for _ in range(self.var.getValue()):
            for ti in self.testItems:
                res += '\t' + ti.__str__()

        return res + '\n'



class Variable(TestItem):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def generate(self):
        return f'{self.value}\n'

    def __str__(self):
        return f'{self.name}: {self.value}\n'
    
    def getValue(self):
        return self.value

    def getName(self):
        return self.name



class RandomVariable(Variable):
    def __init__(self, name, interval):
        a, b = interval
        self.interval = interval

        super().__init__(name, random.randint(a, b))

    def generate(self):
        a, b = self.interval
        self.value = random.randint(a, b)
        return f'{self.value}\n'

    def __str__(self):
        return f'{self.name}: [{self.interval[0]}, {self.interval[1]}]\n'



class RandomArray(TestItem):
    def __init__(self, var, interval):
        self.var = var
        self.interval = interval
        self.arr = []
    
    def generate(self):
        res = ""
        self.arr = []
        #self.var.generate()
        for i in range(self.var.getValue()):
            a, b = self.interval
            val = random.randint(a, b)
            self.arr.append(val)
            res += f'{val} '
        
        return res + '\n'

    def __str__(self):
        return f'Array len {self.var.getValue()} vals {self.interval}'
