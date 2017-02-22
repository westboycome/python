import re
import os
import time

image_path = 'E:\github-project\1.jpg'
dir_path = 'E:\github-project\python'
file_abs_path = 'E:\github-project\python\test.txt'

def getcwd():
    return os.getcwd()

def listdir(dir_path):
    if os.path.exists(dir_path):
        return os.listdir(dir_path)
    else:
        return '目录'+ dir_path + '不存在'

def isfile(file_path):
    if os.path.exists(file_path):
        return os.path.isfile(file_path)
    else:
        return '文件' + file_path + '不存在'

if __name__ == '__main__':
    print('目录空间是：{0}'.format(getcwd()))
    print('文件及目录:',listdir(getcwd()))
    print(listdir('E:\github-project'))
    print(isfile(image_path))
    print('#'*20)
    array = os.path.split(image_path)
    print(array)

    file_full_name = array[1]
    name = os.path.splitext(file_full_name)
    file_name = name[0]
    file_ext =  name[1]
    print('文件全名:{0},文件名：{1},文件后缀：{2}'.format(file_full_name, file_name, file_ext))
    #创建空文件夹
    #os.mkdir('E:\github-project')
    # 创建多级目录
    #os.makedirs('')
    fp = open(file_abs_path, 'w+')
    content = 'this is a test message!!\ngood boy!\ngogo......\nhello,I\'m Hongten\nwelcome to my space!'
    fp.write(content)
    fp.flush()
    fp.close()
    fp = open(file_abs_path, 'r+')
    print('读取文件：{0}所有内容：{1}'.format(file_abs_path, fp.readlines()))

