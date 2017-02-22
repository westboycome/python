#!/usr/bin/python
import os
import re
from  collections import *
def get_worlds(path):
    '''读取一个文件中的内容，返回该文件中的所有单词'''
    if os.path.exists(path):
        return  re.findall(r'\w+',open(path).read().lower())
    else:
        print('the path [{}] is not exist!'.format(path))

def get_most_common_worlds(worlds, number):
    '''如果<code>number > 0</code>,则返回该单词组中出现最多的前<code>number</code>个单词
    否则，返回该单词组中所有统计情况
    '''
    if number > 0:
        return  Counter(worlds).most_common(number)
    else:
        return Counter(worlds)

def main():
    temp_path = 'E:\github-project\python\\test.txt'
    number = 5
    words = get_worlds(temp_path)
    print(words)
    print('#'*50)
    cnt = get_most_common_worlds(words, -1)
    print(cnt)
    print('#'*50)
    cnt = get_most_common_worlds(words, number)
    print(cnt)

if __name__ == '__main__':
    main()