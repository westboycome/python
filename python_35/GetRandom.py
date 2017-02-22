import random
def get_random():
    return random.random()

def get_uniform(a, b):
    return  random.uniform(a,b)

def get_randrange(n):
    return random.randrange(n)

def get_randrange_ex(start, stop, step):
    return random.randrange(start, stop, step)

def shuffle(itmes):
    random.shuffle(itmes)
    return itmes

def sample(itmes, n):
    return random.sample(itmes, n)

def main():
    print('0-1:',get_random())
    print('uniform(a,b):',get_uniform(1,100))
    print('输出的是正整数randrange(n):',get_randrange(800))
    print('返回一个从start开始到stop结束，步长为step的随机数:',get_randrange_ex(0,100,5))

    tem_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print('对一个序列进行洗牌的操作:', shuffle(tem_items))
    temp_list = sample(tem_items[:], 4)
    print('从{}中随机抽出4个数：{}'.format(tem_items, temp_list))


if __name__ == '__main__':
    main()