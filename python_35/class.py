class GrandPa():
    def __init__(self):
        print('I\'m GrandPa')

class Father(GrandPa):
    def __init__(self):
        print('I\'m Father')

class Son(Father):
    i = 12345
    def __init__(self):
        print('这是构造函数，son')
    def sayHello(self):
        return  'hello wprld'

if __name__ == '__main__':
    son = Son()
    print('类型帮助信息:', Son.__doc__)
    print('类型名称：', Son.__name__)
    print('继承的基类:', Son.__bases__)
    print('类型字典:', Son.__dict__)
    print('类型模块:', Son.__module__)
    print('实列类型:', Son.__class__)
