# 获取今日头条一川道的图片




# #########         as异步加载的问题未解决，主要为在python中执行js代码
import requests
from lxml import etree
import urllib.request
import os

url = "http://www.toutiao.com/c/user/article/"

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


params = {
    'page_type': '1',
    'user_id': '7005714682',
    'max_behot_time': '0',
    'count': '20',
    'as': '479BB4B7254C150',
    'cp': '7E0AC8874BB0985'
}


def getxpath(html):
    return etree.HTML(html)


def download(arr, title):
    if title:
        os.mkdir("/home/wangxy/Desktop/123/" + str(title))
    for imgurl in arr:
        print(imgurl)
        # 通过urllib读取地址内容
        img = urllib.request.urlopen(imgurl).read()
        # 拼接图片名字，包括格式
        file_name = imgurl.split('/')[-1].replace('20%', '') + '.jpg'
        # open函数会打开指定路径，存在该文件则打开，不存在则创建后再打开
        if title:
            file = open("/home/wangxy/Desktop/123/"+str(title) + '/' + file_name, 'wb')
        else:
            file = open("/home/wangxy/Desktop/123/" + '/' + file_name, 'wb')
        # 将图片信息写入到本地
        file.write(img)
        # 关闭资源
        file.close()


def get_firstUrl():
    response = requests.get(url=url, params=params, headers=params)
    s = response.json()
    detail_url_0 = []
    for i in range(20):
        detail_url_0.append(s["data"][i]['source_url'].split('/')[2])
    return detail_url_0


def get_img(param):
    newurl = "http://www.toutiao.com/i" + str(param)
    print(newurl)
    response = requests.get(url=newurl, headers=headers)
    s = getxpath(response.content)
    title = s.xpath('//div[@id="article-main"]//h1/text()')
    detail_imgurl = []
    for i in s.xpath('//div[@class="article-content"]//img/@src'):
        detail_imgurl.append(i)
    download(detail_imgurl, title)


if __name__ == "__main__":
    list = []
    list = get_firstUrl()
    for i in list:
        get_img(i)




