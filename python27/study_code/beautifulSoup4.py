import bs4
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html)
#print soup.prettify()
print soup.title
print soup.head
print soup.a
print soup.p
print type(soup.a)
print soup.name
print soup.head.name
print soup.p.attrs
print soup.p['class']
print soup.p.get('class')

print soup.p.string
if type(soup.a.string) == bs4.element.Comment:
    print soup.a.string

print soup.head.contents
print soup.head.children
for child in soup.body.children:
    print child

for child in soup.descendants:
    print child.string

for string in soup.stripped_strings:
    print string

for string in soup.strings:
    print (repr(string))

print soup.p.next_sibling
print soup.p.prev_sibling

print soup.head.next_element
print soup.head.next_elements