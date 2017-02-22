import os
import time

#指定盘符
DESK = 'E:\\'
SAVE_FILE = 'E:\github-project\info.txt'
FILE_EXT =  ['bmp', 'jpeg', 'gif', 'psd', 'png', 'jpg']

my_dirs = []
my_files = []
FILES_NUMBER = 0
RIGHT_FILES_NUMBER = 0
NOT_RIGHT_FILES_NUMBER = 0
DIR_NUMBER = 0

#获取指定文件夹下面的所有文件及文件夹
#如果指定的文件夹不存在，则返回相应的提示信息
def listdir(dir_path):
    if os.path.exists(dir_path):
        return os.listdir(dir_path)
    else:
        return '目录'+ dir_path + '不存在'

#搜索文件主函数
def search_files(path, name):
    if not os.path.isdir(path) and not os.path.isfile(path):
        return  False
    path = os.path.join(path, name)
    if os.path.isfile(path):
        global  FILES_NUMBER
        FILES_NUMBER = FILES_NUMBER + 1
        lists = path.split('.')
        file_ext = lists[-1]
        if file_ext in FILE_EXT:
            global  RIGHT_FILES_NUMBER
            RIGHT_FILES_NUMBER = RIGHT_FILES_NUMBER + 1
            global  my_files
            now = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            size = str(get_file_size(path))
            my_files.append(now+' '+path+' '+size+'\n')
            print('文件:', path)
        else:
            global NOT_RIGHT_FILES_NUMBER
            NOT_RIGHT_FILES_NUMBER = NOT_RIGHT_FILES_NUMBER + 1
    elif os.path.isdir(path):
        global DIR_NUMBER
        DIR_NUMBER = DIR_NUMBER +1
        for name in listdir(path):
            search_files(path, name)

def get_file_size(path):
    if os.path.exists(path):
        return os.path.getsize(path)

def write_info(content):
    if os.path.exists(path):
        with open(SAVE_FILE, 'w+') as fp:
            fp.write(content)
            fp.flush()
            fp.close()
    else:
        print('文件：{}不存在！'.format(SAVE_FILE))

def read_info():
    if os.path.exists(path):
        with open(SAVE_FILE, 'r+') as fp:
            for line in fp:
                print(line)
    else:
        print('文件：{}不存在！'.format(SAVE_FILE))

if __name__ == '__main__':
    for d in listdir(DESK):
        my_dirs.append(os.path.join(DESK, d))
    print(my_dirs)
    my_dir = 'D:\\'
    my_dir = my_dir.split(',')
    print(my_dir)
    for path in my_dir:
        print(path+'aa')
        #search_files(path, '')
    print('#'*50)
    print(my_files)
    print('#' * 50)
    print('开始写入信息---')
    content = ''.join(my_files)
    write_info(content)
    print('#' * 50)
    print('开始读取信息')
    read_info()
    print('#' * 50)
    print('搜索文件夹总数：{0},文件总数：{1}'.format(DIR_NUMBER, FILES_NUMBER))
    print('符合要求的文件总数：{0},不符合要求的文件总数：{1}'.format(RIGHT_FILES_NUMBER, NOT_RIGHT_FILES_NUMBER))


