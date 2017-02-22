#wrap(text, width = 70, **kwargs):这个函数可以把一个字符串拆分成一个序列
from textwrap import *
def test_wrap():
    test_str = '''\
          The textwrap module provides two convenience functions, wrap() and fill(), as well as 1
          TextWrapper, the class that does all the work, and two utility functions, dedent() and indent(). If 2
          you’re just wrapping or filling one or two text strings, the convenience functions should be good 3
          enough; otherwise, you should use an instance of TextWrapper for efficiency. 4
         '''
    print(wrap(test_str,20))

def main():
    test_wrap()
if __name__ == '__main__':
    main()
