from TestGenerator import *
from TestItem import *

x = RandomVariable('x', (1, 10))
r = RepeatContainer('r', x)
y = RandomVariable('y', (10, 20))
a = RandomArray(y, (0, 1))

r.addItem(y)
r.addItem(a)

test = Test('abc')
test.addItem(x)
test.addItem(r)

#print(test.variables[0], test.repeaters[0])

gen = TestGenerator(test)
gen.generate(5)

