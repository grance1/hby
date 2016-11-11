def fact(n):
    if n== 1:
        return 1
    return n * fact(n - 1)
print fact(1)
print fact(5)
print fact(100)
print int('123')
print int('123',8)
print int('123',10)
def pow(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print pow(5)


def greet(name='world'):
        print 'Hello,'+ name+'.'
print greet()
print greet('Bart')


