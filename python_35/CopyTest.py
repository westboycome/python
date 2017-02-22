import copy
def shallow_copy(s):
    return copy.copy(s)

def deep_copy(d):
    return copy.deepcopy(d)

def test_shallow():
    tmp_data = ['a', 'b', 'c', 'y', [1, 2, 3]]
    print('原来的数据:{}'.format(tmp_data))
    s_copy = shallow_copy(tmp_data)
    tmp_data.append('xiaoheizi')
    tmp_data[4].append('4')
    print('修改后:{}'.format(tmp_data))
    print('拷贝的数据:{}'.format(s_copy))

def test_deep():
    tmp_data = ['a', 'b', 'c', 'y', [1, 2, 3]]
    print('原来的数据:{}'.format(tmp_data))
    s_copy = deep_copy(tmp_data)
    tmp_data.append('xiaoheizi')
    tmp_data[4].append('4')
    print('修改后:{}'.format(tmp_data))
    print('拷贝的数据:{}'.format(s_copy))

def main():
    test_shallow()
    print('#'*50)
    test_deep()

if __name__ == '__main__':
    main()