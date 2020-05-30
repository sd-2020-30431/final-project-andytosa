from TestGenerator import *
from TestItem import *

x = RandomVariable('x', (1, 10))
r = RepeatContainer(x)
y = RandomVariable('y', (10, 20))
a = RandomArray(y, (0, 1))

r.addItem(y)
r.addItem(a)

test = Test('abc')
test.addItem(x)
test.addItem(r)

gen = TestGenerator(test)
gen.generate(5)

