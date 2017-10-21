# 获取www.579ss.com的图片
import requests
from lxml import etree
import urllib.request
import os

url = 'http://1122iz.com/tupianqu/yazhou/index_'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': '3344at.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}


def getxpath(html):
    return etree.HTML(html)


# 下载到本地的函数
def download(arr, title):
    os.mkdir("/home/wangxy/Desktop/0/" + str(title))
    for imgurl in arr:
        print(imgurl)
        img = urllib.request.urlopen(imgurl).read()
        # 拼接图片名字，包括格式
        file_name = imgurl.split('/')[-1].replace('20%', '')
        # open函数会打开指定路径，存在该文件则打开，不存在则创建后再打开
        file = open("/home/wangxy/Desktop/1/"+ str(title) + '/' + file_name, 'wb')
        # 将图片信息写入到本地
        file.write(img)
        # 关闭资源
        file.close()


def geturls(newurl):
    response = requests.get(newurl, headers)
    print(response.status_code)
    s = getxpath(response.content)
    print(response.url)
    print("======================")
    list_urls = []
    list_urls = s.xpath('//ul[@class="news_list"]//a/@href')
    print(list_urls)
    return list_urls


def getimg(detailUrl):
    response = requests.get(detailUrl, headers)
    s = getxpath(response.content)
    print(detailUrl)
    print(response.url)
    print('=================')
    img_urls = []
    title = s.xpath('//div[@class="main"]//h1/text()')
    img_urls = s.xpath('//div[@class="news"]//img/@src')
    print(title)
    print(len(img_urls))
    download(img_urls, title)


if __name__ == "__main__":
    for j in range(5, 7):
        list = []
        newurl = url + str(j) + '.html'
        list = geturls(newurl)
        for i in list:
            detailUrl = 'http://1122ur.com' + i
            getimg(detailUrl)

