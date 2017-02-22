import fileinput
import os

def get_file_content(files):
    if files !=None:
        lines = ''
        with fileinput.input(files) as fp:
            for line in fp:
                lines += line
            return lines
    else:
        print('files isNone')

def get_file_name(file):
    if os.path.exists(file) and os.path.isfile(file):
        names = []
        for line in fileinput.input(file):
            name = fileinput.filename()
            if name != None:
                fileinput.nextfile()
            names.append(name)
        return names
    else:
        print('the path [{}] is not exits!'.format(file))

def main():
    files = ('E:\github-project\python\\test.txt', 'E:\github-project\python\\pathTest.py')
    file = 'E:\github-project\python\\test.txt'
    content = get_file_content(files)
    print(content)
    name = get_file_name(file)
    print(name)

if __name__ == '__main__':
    main()