# 获取www.579ss.com的图片
import requests
from lxml import etree
import urllib.request

url = 'http://1122hi.com/tupianqu/yazhou/index_'

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


def getxpath(html):
    return etree.HTML(html)


# 下载到本地的函数
def download(arr):
    for imgurl in arr:
        print(imgurl)
        img = urllib.request.urlopen(imgurl).read()
        # 拼接图片名字，包括格式
        file_name = imgurl.split('/')[-1].replace('20%', '')
        # open函数会打开指定路径，存在该文件则打开，不存在则创建后再打开
        file = open("/home/wangxy/Desktop/123" + '/' + file_name, 'wb')
        # 将图片信息写入到本地
        file.write(img)
        # 关闭资源
        file.close()


def geturls(newurl):
    response = requests.get(newurl, headers)
    print(response.status_code)
    s = getxpath(response.content)
    list = []
    list = s.xpath('//ul[@class="news_list"]//a/@href')
    print(list)
    return list


def getimg(detailUrl):
    response = requests.get(detailUrl, headers)
    s = getxpath(response.content)
    list = []
    list = s.xpath('//div[@class="news"]//img/@src')
    print(len(list))
    download(list)


if __name__ == "__main__":
    for j in range(15):
        list = []
        x = j + 2
        newurl = url + str(x) + '.html'
        print(newurl)
        list = geturls(newurl)
        for i in list:
            detailUrl = 'http://1122ur.com' + i
            getimg(detailUrl)

