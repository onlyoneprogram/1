import parsel
from parsel import Selector
import requests
import js2xml

heads = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #'Accept': 'application/json',
    #'X-Request': 'JSON',
    #'X-Requested-With': 'XMLHttpRequest'
}



detailurl='http://huaban.com/pins/1062650100/'
z3 = requests.get(url=detailurl, headers=heads)
sel1 = Selector(text=z3.text)
# print(z3.status_code)
# 获取所有的//script
# print(sel1.xpath('//script/text()'))
# 获取我们需要的那一段，匹配唯一的字段即可 app.page = app.pag
# 注意，在代码中编辑字段时候原字段是什么格式，代码中应保持一致，否则匹配失败，例如空格
# print(sel1.xpath('//script[contains(.,"app.page=app.pag")]/text()'))
# print(sel1.xpath('//script[contains(.,"app.page = app.pag")]/text()'))
# 获取jscode,也就是我们需要抓取的那一段
jscode = sel1.xpath('//script[contains(.,"app.page = app.pag")]/text()').extract_first()
# 使用js2xml将js代码转变为xml
parsed_js = js2xml.parse(jscode)
# 打印测试
# print(js2xml.pretty_print(parsed_js))
# 获取图片地址
# print(parsed_js.xpath('//property[@name="key"]/string/text()'))
# print(len(parsed_js.xpath('//property[@name="key"]/string/text()')))

import urllib.request


for i in parsed_js.xpath('//property[@name="key"]/string/text()'):
    imgurl = 'http://img.hb.aicdn.com/'+i
    print(imgurl)
    img = urllib.request.urlopen(imgurl).read()
    file_name = imgurl.split('/')[-1].replace('20%', '')+'.jpg'
    file = open("/home/wangxy/Desktop/tupian"+'/'+file_name, 'wb')
    file.write(img)
    file.close()

#import time
#imgurl = 'http://img.hb.aicdn.com/b78109d2a32117fb9536b3ffedb285e83024ba319b11-Ai442L_fw658'
#i = time.time()
#img = urllib.request.urlopen(imgurl).read()
#print('耗时:'+str(int(time.time()-i))+'s')
#print(img)
#file_name = imgurl.split('/')[-1].replace('20%', '')+'.jpg'
#print(file_name)
#open("/home/wangxy/Desktop/text.txt", 'wb')
#file = open("/home/wangxy/Desktop"+'/'+file_name, 'wb')
#file.write(img)
#file.close()








