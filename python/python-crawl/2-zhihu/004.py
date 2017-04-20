#coding=utf-8

from tkinter import * #GUI(图像用户界面)模块

from ScrolledText import ScrolledText #文本滚动条

import urllib,requests #请求模块

import re #正则表达式

import threading #多线程处理与控制

url_name = []#url+name

a = 1#页码

def get():

global a #全局变量

hd = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

url = '视频短剧_搞笑视频_恶搞视频－百思不得姐官网，第1页'+str(a)

varl.set('已结获取到第%s页视频'%(a))

html = requests.get(url,headers=hd).text #获取源码

a += 1

url_content = re.compile(r'<div class="j-r-list-c">.*?</div>.*?</div>',re.S)

url_contents = re.findall(url_content,html)

#print url_contents

for i in url_contents:

url_reg = r'data-mp4="(.*?)">'#匹配地址

url_items = re.findall(url_reg,i)

#print url_items #视频列表

if url_items:#判断地址列表是否存在

name_reg = re.compile(r'<a href="/detail-.{8}?.html"(.*?)</\w>',re.S)

name_items = re.findall(name_reg,i)

#print name_items #名字列表

for i,k in zip(name_items,url_items):

url_name.append([i,k])

print i,k

return url_name

id = 1#视频

def write():

global id

while id<10:

url_name = get()

for i in url_name:#名字+地址

#aa = i[0].decode('utf-8').encode('gbk')

urllib.urlretrieve(i[1],'video\\%s.mp4'%(a))

text.insert(END,str(id)+'.'+i[1]+'\n'+i[0]+'\n')

url_name.pop(0)

id += 1

varl.set('视频链接和名字抓取完毕,over')

def start():

th = threading.Thread(target=write)

th.start()#触发

root = Tk()

root.title('爬取某视频')

root.geometry('666x525')

text = ScrolledText(root,font=('微软雅黑',10))

text.grid() #布局的方法 pack简单

button = Button(root,text='开始爬取',font=('微软雅黑',10),command=start)

button.grid()

varl = StringVar()

label = Label(root,font=('微软雅黑',10),fg='red',textvariable = varl)

label.grid()

varl.set('已准备...')

root.mainloop()#发送创建窗口的指令