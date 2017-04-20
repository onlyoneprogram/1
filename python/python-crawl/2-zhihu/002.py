# 爬取廖雪峰教程的标题

import requests
from lxml import etree

url = 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}


def getxpath(html):
    return etree.HTML(html)

z = requests.get(url, headers)
s = getxpath(z.content)
list = []
list = s.xpath("//ul[@style='margin-right:-15px;']//a/text()")
for i in list:
    print(i)