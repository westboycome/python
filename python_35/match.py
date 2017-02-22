#!/usr/bin/python
import re
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*)are(.*?).*',line,re.M|re.I)
ma = re.match(r'dogs', line, re.M | re.I)
se = re.search(r'dogs', line , re.M | re.I)
if matchObj:
    print ("matchObj.group():",matchObj.group())
    print ("matchObj.group(1):",matchObj.group(1))
    print ("matchObj.group(2):",matchObj.group(2))
else:
    print ("No match!")
if ma:
    print(ma.group())
elif se:
    print(se.group())

#修饰符	描述
#re.I	使匹配对大小写不敏感
#re.L	做本地化识别（locale-aware）匹配
#re.M	多行匹配，影响 ^ 和 $
#re.S	使 . 匹配包括换行在内的所有字符
#re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
#re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)
print ("Phone Num : ", num )
