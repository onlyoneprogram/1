import requests
import lxml
from lxml import etree

url = 'https://www.zhihu.com/#signin'
headers = {
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
z = requests.get(url, headers = headers)
print(z.status_code)

sel = etree.HTML(z.content)
_xsrf = sel.xpath('//input[@name="_xsrf"]/@value')[0]
print(_xsrf)

loginurl = 'https://www.zhihu.com/login/phone_num'
fromdata = {
    'phone_num':'18180544256',
    'password':'wxy890125!',
    '_xsrf':'_xsrf'
}

z2 = requests.post(url=loginurl, data=fromdata, headers=headers)
print(z2.status_code)
print(z2.content)
print(z2.json()['msg'])
# 登陆失败，因为验证码没有做好验证

mylog = 'https://www.zhihu.com/people/pa-chong-21/logs'
z3 = requests.get(url=mylog, headers=headers)
print(z3.status_code)
print(z3.text)
print(z3.url)
