#import fibo

#fibo.fib(100)
#print(fibo.fib2(100))
import math
from fibo import *
fib(100)
print(fib2(1000))
print(add(1, 2))

for i in range(5):
    print(i)

print([i for i in range(5, 100,20)])
#使用'{}'占位符
print('I\'m {},{}'.format('Hongten','Welcome to my space!'))
#也可以使用'{0}','{1}'形式的占位符
print('{0},I\'m {1},my E-mail is {2}'.format('Hello','Hongten','hongtenzone@foxmail.com'))

print('{}.'.format(math.pi))
print('{!r}.'.format(math.pi))
print('{0:3f}.'.format(math.pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))
