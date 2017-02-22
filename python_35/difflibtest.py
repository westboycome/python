from  difflib import *
import  os
def write():
    if os.path.exists('E:\github-project\python'):
        with open('E:\github-project\python','w+') as fp:
            test = HtmlDiff.make_file(HtmlDiff(), 'hello world!', 'hElLO Wor2d！')
            fp.write(test)
            print('生成文件成功')
            fp.close()

def main():
    write()

if __name__ == '__main__':
    main()