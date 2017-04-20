# coding: UTF-8
import os
import sys
import requests
import urllib.request,io
from html.parser import HTMLParser

#全局变量

id_list = set()         #保存视频ID的列表
id_dict = {}            #保存id和对应子视频数目
cookies = {}            #保存cookies


# HTML解析类
class MyHTMLParser(HTMLParser):
    def __init__(self, key, attr):
        HTMLParser.__init__(self)
        self.links = []
        self.keys = key
        self.attr = attr



    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        #if tag == "source":
        if tag == self.keys:
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    #if variable == "src":
                    if variable == self.attr:
                        self.links.append(value)


# 解析cookies字典
def getCookies(cookies_str):
    global cookies
    for line in cookiesStr.split(';'):
        #其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies[name] = value


def getHtml(url, key, value):
    global cookies
    r = requests.get(url, cookies=cookies)
    content = r.content.decode('UTF-8')
    hp = MyHTMLParser("source", "src")
    hp.feed(content)
    hp.close()
    print(hp.links)
    for link in hp.links:
        link_str = str(link)
        if link_str.find(".mp4") >= 0:
           downloadFile(link, key, value)
        else:
           print("没有找到对应视频")


#获取课程数目
def getCourseNum(url):
    global cookies
    url_list = set()
    r = requests.get(url, cookies=cookies)
    content = r.content.decode('UTF-8')
    hp = MyHTMLParser("a", "href")
    hp.feed(content)
    hp.close()
    for link in hp.links:
        link_str = str(link)
        if link_str.find("http://www.jikexueyuan.com/course/") >= 0 and link_str.find(".html?ss=1") >= 0:
            url_list.add(link_str)
    return url_list.__len__()


#获取所有视频ID，根据目录网页
def getIdList(root):
    global cookies
    r = requests.get(root, cookies=cookies)
    content = r.content.decode('UTF-8')
    hp = MyHTMLParser("a", "href")
    hp.feed(content)
    hp.close()
    #print(hp.links)
    #声明引用全局id_list,在最上面定义
    global id_list
    global id_dict

    for link in hp.links:
        link_str = str(link)
        if link_str.find("http://www.jikexueyuan.com/course/") >= 0 and link_str.find(".html")>= 0:
            #print(link)
            c_id = link_str.lstrip("http://www.jikexueyuan.com/course/").rstrip(".html")
            if c_id not in id_list:
                id_dict[c_id] = getCourseNum(link_str)
                print(c_id, id_dict[c_id])
            id_list.add(c_id)
    print(id_dict)

def downloadFile(url, key, value):
    #url = 'http://cv4.jikexueyuan.com/10de45bbf83e450ff5e11ff4599d7166/201603202253/cocos2d-x/course_712/01/video/c712b_01_h264_sd_960_540.mp4'
    r = requests.get(url)
    file_name = str(key)+"_"+str(value)+".mp4"
    with open(file_name, "wb") as code:
         code.write(r.content)

if __name__=="__main__":
    count = 0
    #解析cookies 利用免费时间下载需要视频，需要账号的cookies
    cookiesStr = "通过谷歌浏览器可以获取"
    getCookies(cookiesStr)


    root = "http://ke.jikexueyuan.com/xilie/331?huodong=shequn_0307"
    getIdList(root)

    head = "http://www.jikexueyuan.com/course/"

    for key in id_dict:
        if id_dict[key] <= 0:
            print(id_dict[key],"没有数据")
            break
        for i in range(1, id_dict[key]+1):
            url = head+key+"_"+str(i)+".html?ss=1"
            print("下载:")
            print(url)
            count += 1
            getHtml(url, key, i)
    print("视频总数：")
    print(count)