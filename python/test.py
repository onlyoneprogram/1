# -*- coding: utf-8 -*-
import requests
import js2xml
from lxml import etree

headers = {
    # 这边cookie替换成你的cookie
    'Cookie': '',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19',
}


# 获取红包列表
def getuid():
    url = 'http://chunjie.hongbao.weibo.com/hongbao2017/h5index'
    # 带上request headers
    z = requests.get(url, headers=headers)
    if z.status_code == 200:
        # 这边是查找所有的ouid
        alluid = etree.HTML(z.content).xpath('//div[@class="m-auto-box"]/@action-data')
        return alluid


# 获取st的值
def getst(url):
    # 带上request headers
    z = requests.get(url, headers=headers)
    # 获取第一段JavaScript,并去掉 <!--拆包页-->，防止中文报错
    jscode = etree.HTML(z.content).xpath("//script[contains(., 'weibo')]/text()")[0].replace(u'<!--拆包页-->', '')
    # 使用js2xml 把JavaScript代码替换成xml
    parsed_js = js2xml.parse(jscode)
    # 打印下 xml
    # print js2xml.pretty_print(parsed_js)

    # 从上面可以看到st在哪，然后用xpath写出来
    st = parsed_js.xpath('//property[@name="st"]/string/text()')[0]
    return st


# 抢红包
def tj(url, uid, st, tjheaders):
    # 生成需要发送的data
    data = {
        'groupid': '1000110',
        'uid': uid,
        'share': '1',
        'st': st
    }
    # 这里使用了post,headers增加了Referer
    z = requests.post(url, data=data, headers=tjheaders)
    # 把得到的结果以json形式展示
    _ = z.json()
    # 如果json中有“ok”,表示提交成功了，否则返回报错信息
    if _.has_key('ok'):
        print(_['data']['error_msg'])
    else:
        print(_['errMsg'])


if __name__ == '__main__':
    # 得到所有的uid
    uids = getuid()
    for uid in uids:
        # 生成红包页面的url
        url = 'http://hongbao.weibo.com/h5/aboutyou?groupid=1000110&ouid=%s' % uid
        # 获取st
        st = getst(url)
        # 生成点击“抢红包”页面的url
        tjurl = 'http://hongbao.weibo.com/aj_h5/lottery?uid=%s&groupid=1000110&wm=' % uid
        # 添加Referer，如果不添加会报错
        headers['Referer'] = url
        tjheaders = headers
        try:
            # 点击“抢红包”
            tj(tjurl, uid, st, tjheaders)
        except:
            pass