import os
import time
import stat
import bs4

def print_info(file):
    if file != None:
        file_info = {
            'Size': file[stat.ST_SIZE],
            'LastModified': time.ctime(file[stat.ST_MTIME]),
            'LastAccessed': time.ctime(file[stat.ST_ATIME]),
            'CreateionTime': time.ctime(file[stat.ST_CTIME]),
            'Mode': file[stat.ST_MODE],
            'Device': file[stat.ST_DEV],
            'UserId': file[stat.ST_UID],
            'GroupId': file[stat.ST_GID]
        }
        for key in file_info:
            print('{}:{}'.format(key, file_info(key)))
    else:
        print('None')

def main():
    file = 'E:\github-project\python\\test.txt'
    print(print_info(file))
    print(bs4)

if __name__ == '__main__':
    main()