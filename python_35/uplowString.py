#字母大小写转换
#首字母转大写
#去除字符串中特殊字符(如：'_'，'.'，','，';')，然后再把去除后的字符串连接起来
#!/usr/bin/python
low_strs = 'abcd'
uper_strs = 'DEG'
test_strA = 'hello_fjghfhj'
test_strB = 'fhjdhgjFHjgf'
test_strC = 'ghfg_jhf_hjfh_dkjfh_fd'
test_strD = 'gjfh__fn_f_f_'

print('小写转大写:',low_strs.upper())
print('大写转小写:',uper_strs.lower())
test_strB = test_strB[0].upper()+test_strB[1:]
print('只大写第一个字母:',test_strB)
test_strA = ''.join(test_strA.split('_'))
print('去掉中间的_:',test_strA)

# 去除'test_strC'中的'_',并且把从第一个'_'以后的单词首字母大写
def get_str(oriStr, splitStr):
    str_list = oriStr.split(splitStr)
    if len(str_list) > 1:
        for index in range(1, len(str_list)):
            if str_list[index] != '':
                str_list[index] = str_list[index][0].upper() + str_list[index][1:]
            else:
                continue
        return ''.join(str_list)
    else:
        return oriStr

print('去除\'\'ghfg_jhf_hjfh_dkjfh_fd中的\'_\',并且把从第一个\'_\'以后的单词首字母大写:',get_str(test_strC, '_'))
print('去除\'\'gjfh__fn_f_f_中的\'_\',并且把从第一个\'_\'以后的单词首字母大写:',get_str(test_strD, '_'))


