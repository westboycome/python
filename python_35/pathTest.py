import os
def abspath(path):
    return os.path.abspath(path)

def dirname(path):
    '''返回文件路径'''
    return os.path.dirname(path)

def getatime(path):
    '''最后修改时间'''
    return os.path.getatime(path)

def getctime(path):
    return os.path.getctime(path)

def getsize(path):
    return os.path.getsize(path)

def is_file(path):
    return os.path.isfile(path)

def is_dir(path):
    return os.path.isdir(path)

def is_link(path):
    return os.path.islink(path)

def splitext(path):
    return os.path.split(path)

def splitunc(path):
    return os.path.splitunc(path)

def split(path):
    return os.path.split(path)

def main():
    tmp_path = 'E:\github-project\python\\test.txt'
    print(abspath(tmp_path))
    print(dirname(tmp_path))
    print(getatime(tmp_path))
    print(getctime(tmp_path))
    print(getsize(tmp_path))
    print(split(tmp_path))
    print(splitunc(tmp_path))
    print(splitext(tmp_path))

if __name__ == '__main__':
    main()