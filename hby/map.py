def f(x):
    return x.capitalize()
r = map(f, ['adam','LISA','barT'])

print r

from functools import reduce
def prod(x, y):
    return x * y
print reduce(prod, [1, 3, 5, 7, 9])