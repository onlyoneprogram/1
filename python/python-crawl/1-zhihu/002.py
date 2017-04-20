from lxml import etree

# 定义一个函数，给它一个html，返回xml结构
def getxpath(html):
    return etree.HTML(html)


# 下面是我们是战得第一个html
sample = """<html>
    <head>
        <title>page</title>
    </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <!-- this is the end -->
  </body>
</html>
"""

# 获取xml结构

s1 = getxpath(sample)


# 获取标题 两种办法都是可以的
print(s1.xpath('//title/text()'))
print(s1.xpath('/html/head/title/text()'))

print(s1.xpath('//@href'))
print(s1.xpath('//@src'))
print(s1.xpath('//h2/text()'))



sample2 = """
<html>
  <body>
    <ul>
      <li>Quote 1</li>
      <li>Quote 2 with <a href="...">link</a></li>
      <li>Quote 3 with <a href="...">another link</a></li>
      <li><h2>Quote 4 title</h2> ...</li>
    </ul>
  </body>
</html>
"""
s2 = getxpath(sample2)

print(s2.xpath('//li[1]/text()'))


sample3 = """<html>
  <body>
    <ul>
      <li id="begin"><a href="https://scrapy.org">Scrapy</a>begin</li>
      <li><a href="https://scrapinghub.com">Scrapinghub</a></li>
      <li><a href="https://blog.scrapinghub.com">Scrapinghub Blog</a></li>
      <li id="end"><a href="http://quotes.toscrape.com">Quotes To Scrape</a>end</li>
      <li data-xxxx="end" abc="abc"><a href="http://quotes.toscrape.com">Quotes To Scrape</a>end</li>
    </ul>
  </body>
</html>
"""
s3 = getxpath(sample3)

print(s3.xpath('//li/a[@href="https://scrapy.org"]/text()'))
print(s3.xpath('//li[@abc="abc"]/text()'))
print(s3.xpath('//li[@id="begin"]/text()'))


sample4 = u"""
<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <p class="test">
    编程语言<a href="#">python</a>
    <img src="#" alt="test"/>javascript
    <a href="#"><strong>C#</strong>JAVA</a>
    </p>
    <p class="content-a">a</p>
    <p class="content-b">b</p>
    <p class="content-c">c</p>
    <p class="content-d">d</p>
    <p class="econtent-e">e</p>
    <p class="heh">f</p>
    <!-- this is the end -->
  </body>
</html>
"""
s4 = etree.HTML(sample4)

print(s4.xpath('//p[@class="content-a"]/text()'))
print(s4.xpath('//p[@class="test"]/text()'))
# string获取某个标签下所有的文本
print(s4.xpath('string(//p[@class="test"])'))
# starts-with 匹配字符串前面相等
# contains 匹配任何位置相等
print(s4.xpath('//p[starts-with(@class,"content")]/text()'))
print(s4.xpath('//p[contains(@class,"content")]/text()'))
print(s4.xpath('//p[@class="heh"]/text()'))
print(s4.xpath('//p[starts-with(@class,"he")]/text()'))
