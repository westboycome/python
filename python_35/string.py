#!/usr/bin/python
import urllib.request
import urllib.parse
import re
import urllib.request,urllib.parse,http.cookiejar
str = "Line1-abscdfefef \nLine2-abcdsd \nline3-fdffdfd"
#print(str.split(' '))
#print(str.split(' ',1))

def getHtml(url):
    cj=http.cookiejar.CookieJar()
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),('Cookie','4564564564564564565646540')]

    urllib.request.install_opener(opener)
    
    html_bytes = urllib.request.urlopen( url ).read()
    html_string = html_bytes.decode( 'utf-8' )
    return html_string

html = getHtml("http://zst.aicai.com/ssq/openInfo/")
table = html[html.find('<table class="fztab nbt">') : html.find('</table>')]
tmp = table.split('<tr \r\n\t\t onmouseout=',1)
trs = tmp[0]
tr = trs[: trs.find('</tr>')]
number = tr.split('<td>')[0].split('</td>')[0]
print(number + '期开奖号码:'  ,end=' ')
redtemp = tr.split('<td class="redColor sz12" >')
reds = redtemp[1:len(redtemp)-1]
for redstr in reds:
    pring(redstr.split('<td>')[0] + ",",end='')
print ("篮球：",end='')
blue = tr.split('td class="blueColor sz12" >')[0].split('/td')[0]
print(blue)

str = "abcdefghil"
str1 = "jhghhb"
n =3
str +=str1[0:n]
print(str)
#print(len(str and 'jh'))
#print(str.upper())
#print(str.lower())

str1 = '12345ff'
str2 = '1234'
n = 3
#print(cmp(str1[0:3],str2[0:n]))
ch = 'r'
str1 = n * ch + str1[3:]
#print(str1)

npos = -1
for c in str1:
    if c in str2:
        npos = str1.index(c)
        break
#print(npos)
#翻转字符串
print(str1[::-1])
#查找
ss = "1234f,dvdf,fd,v,d,f"
print(ss.find(str2))
#分割字符串
print(ss[ss.find(',')+1])
c = ss.split(',')
print(c)

def OnlyCharNum(s,oth=''):
    s4 = s.lower();
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s4:
        if not c in fomart:
            s = s.replace(c,'');
    return s;

print(OnlyCharNum("a000 aa-b"))

strs = '0123456789'
print(strs[0:3])
print(strs[:])
print(strs[6:])
print(strs[:-3])
print(strs[2])
print(strs[-1])
print(strs[::-1])
print(strs[-3:-1])
print(strs[-3:])
print(strs[:-5:-3])
print(strs[:-4:-2])
print(strs[:-6:-2])
