#!/usr/bin/oythin
def myMethod(x,y):
    return x**y
def fib(n):
    a,b = 0, 1
    while a < n:
        print(a, end=' ')
        a,b =  b, a+b

    print()

def getList(oldList, length):
    if length >0:
        for i in range(0, length):
            oldList.append(i)
        return  oldList
    else:
        return '你输入的长度小于0'

def ask_ok(prompt, retries=4, complaint='Yes or no,please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n','no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise  IOError('refusenik user')
        print(complaint)

if __name__ == '__main__':
    x = 3
    y = 4
    n = 20
    print(myMethod(x,y))
    fib(n)
    ask_ok('y')