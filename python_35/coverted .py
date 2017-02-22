#!/url/bin/python
#int(x [,base ])         将x转换为一个整数
#long(x [,base ])        将x转换为一个长整数
#float(x )               将x转换到一个浮点数
#complex(real [,imag ])  创建一个复数
#str(x )                 将对象 x 转换为字符串
#repr(x )                将对象 x 转换为表达式字符串
#eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
#tuple(s )               将序列 s 转换为一个元组
#list(s )                将序列 s 转换为一个列表
#chr(x )                 将一个整数转换为一个字符
#unichr(x )              将一个整数转换为Unicode字符
#ord(x )                 将一个字符转换为它的整数值
#hex(x )                 将一个整数转换为一个十六进制字符串
#oct(x )                 将一个整数转换为一个八进制字符串

#convert to int
print('int()默认情况下为:',int())
print('str字符转换为int:',int('010'))
print('float转int:',int(243.342))
#十进制数10，对应的2进制，8进制，10进制，16进制分别是：1010,12,10,0xa
print(int('0xa',16))
print(int('10',10))
print(int('12',8))
print(int('1010',2))

#convert to long
print(int(23))

#convert to float
print(float())
print(float('323.323'))
print(float(233))

#convert to complex
print('创建一个复数',complex(12,34))
print(complex(23))

#convert to str
print(str())
print(str(323.4343))
print(str(21))
lists = ['q','q','w','w','r']
print(''.join(lists))

#convert to list
strs = 'hongteng'
print(list(strs))

#covert to tuple 
print('列表list转换为tuple:', tuple(lists))

#char coverted to int
print(chr(67))
print(ord('c'))

print('整数转16进制数:', hex(12))
print('整数转8进制数:', oct(12))
