#python列表，数组类型要相同，python不需要指定数据类型，可以把各种类型打包进去
#python列表可以包含整数，浮点数，字符串，对象
#创建列表三种方式：1.member = ["zdz","liufeng","hots"],2.number = [1,2,3],
#3.混合型 mix = [1,'zdz',3.12,[1,2,3]] 4.空列表 empty = []
#向列表添加使用append追加一个元素到末尾，extend追加另外一个列表到末尾，insert插入到指定位置
emptylist = []
#print(emptylist)
mix = [1,'zdz',3.12,1,2,3]
#print(mix)
mix.append("fjdgfjhdg")
#print(mix)
#print(len(mix))

mix.insert(0, "asds")
temp = mix[0]
mix[0] = mix[1]
mix[1] = temp

#从列表里删除元素 remove del pop
#mix.remove("zdz") 必须有值
#del mix[3]
#pop pop(i)  删除最后一个元素，或者指定索引值的元素

cm = mix[1:3]#拷贝
#print(cm)
l1=[123]
l2=[234]
print(l1 > l2)
l1=[123,234]
l2=[234,123]
l3=[123,456]

print(l1 < l2) and (l1 == l3)
print(123 in l3)
print(123 not in l3)
#list 内置函数 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
print(l3.count(123))

#列表反转
l3.reverse()
print(l3)
#排序
l4=[1,4,6,84,24,6,78,43,222,76577,755,4]
l5=l4[:]
l6=l4
l4.sort()
#反向排序
l5.sort(reverse=True)
print(l4)
print(l5)
print(l6)
#print(mix)
