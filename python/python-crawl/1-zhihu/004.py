import js2xml
import urllib.request
import time

# #################获取花瓣照片############
import requests
from parsel import Selector

hburl = 'http://huaban.com/explore/guzhuangmeinv/'
heads = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Accept': 'application/json',
    'X-Request': 'JSON',
    'X-Requested-With': 'XMLHttpRequest'
}

# 第一条数据和第二条数据都是会随着异步加载而改变
params = {
    'j1his8km': '',
    'max': '1070545671',
    'limit': '20',
    'wfl': '1'

#j1his8km:
#max:1070545671
#limit:20
#wfl:1
}


z = requests.get(url=hburl, params=params, headers=heads)
print(z.status_code)

for i in z.json()['pins']:
    print(i["pin_id"])

list = []
for i in z.json()['pins']:
    print((i['file']).get('key'))
    list.append((i['file']).get('key'))

starttime = time.time()
for i in list:
    imgurl = 'http://img.hb.aicdn.com/'+i
    print(imgurl)
    img = urllib.request.urlopen(imgurl).read()
    file_name = imgurl.split('/')[-1].replace('20%', '')+'.jpg'
    file = open("/home/wangxy/Desktop/tupian"+'/'+file_name, 'wb')
    file.write(img)
    file.close()

endtime = time.time()
print(endtime-starttime)





















