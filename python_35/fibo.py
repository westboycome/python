#!/usr/bin/python
# write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

def add(n1, n2):
    return  n1 + n2

def sub(n1, n2):
    return  n1 - n2

def mil(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 != 0:
        return n1/n2
    else:
        return 'Error'