from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 根据HTML网页字符串创建beautifulSoup对象
soup = BeautifulSoup(
    html_doc,                   # Html文档字符串
    'html.parser'              # Html解析器
#    from_encoding='utf-8'       # Html文档的编码
)

links = soup.find_all('a')

#for link in links:
#    print(link.name, link['href'], link.get_text())

link_node = soup.find('a', href='http://example.com/tillie')
#print(link_node)

#print(soup.prettify())

print(soup.title)
print(soup.head)
print(soup.find_all('a'))

print(type(soup.a))
print(soup.name)
print(soup.head.name)
print(soup.a['href'])

soup.p['class']='newClass'
print(soup.p)
del soup.p['class']
print(soup.p)

print(type(soup.p.string))

print(type(soup.name))

print(soup.a)
print(soup.a.string)
print(type(soup.a.string))


print("======================")
print(soup.head.children)
for child in soup.body.children:
    print(child)

print("=======================")
for child in soup.descendants:
    print(child)





