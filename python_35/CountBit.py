from collections import  *
import os
def get_counter():
    '''get the Counter object'''
    return Counter()

def str_to_list(s):
    if s != None:
        return [x for x in s]
    else:
        return []

def counter(c,l):
    '''统计列表l中每个单词的出现次数，最后返回一个Counter对象'''
    for world in l:
        c[world] += 1
    return  c

def get_file_str(path):
    '''打开指定的文件，并且把文件中的内容以字符串的形式返回'''
    if os.path.exists(path):
        temp_str = ''
        with open(path, 'r') as pf:
            for line in pf:
                temp_str += line
            return  temp_str
    else:
        print('the file [{}] is not exist!'.format(path))

def test_str():
    cnt = get_counter()
    temp_str = 'hello,i\'m Hongten,welcome to my space!'
    temp_list = str_to_list(temp_str)
    cnt = counter(cnt, temp_list)
    print(cnt)

def test_file():
    cnt = get_counter()
    temp_path = 'E:\github-project\python\\test.txt'
    temp_str = get_file_str(temp_path)
    temp_list = str_to_list(temp_str)
    cnt = counter(cnt, temp_list)
    print(cnt)


def main():
    test_str()
    print('#'*50)
    test_file()


if __name__ == '__main__':
    main()