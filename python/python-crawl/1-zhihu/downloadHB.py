# #################获取花瓣照片############
import urllib.request
import requests

# 请求地址
hburl = 'http://huaban.com/explore/guzhuangmeinv/'
# 请求头，根据需要添加相应的元素
heads = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Accept': 'application/json',
    'X-Request': 'JSON',
    'X-Requested-With': 'XMLHttpRequest'
}

# 花瓣图片属于异步加载，max数据会根据加载而变化
# 第二次请求所需要的max为上一次请求的最后一个pin_id
params = {
    'j1his8km': '',
    'max': '1070545671',
    'limit': '20',
    'wfl': '1'
}


# 获取pins的方法
# 第一次请求过后下载图片和保存最后一个pin_id
# 下一次更改params中max参数再次请求，达到下拉异步加载的作用，并下载图片
# 记得清空数组
def getpins():
    # 第一次请求
    z = requests.get(url=hburl, params=params, headers=heads)
    # 图片的部分地址，用于download的时候拼接成完整的地址
    list_keys = []
    # 第一次获取到key
    for i in z.json()['pins']:
        list_keys.append((i['file']).get('key'))
    # 下载图片的函数
    download(list_keys)
    while True:
        # 获取最后一次的pin_id
        last_pin_id = z.json()['pins'][-1]['pin_id']
        try:
            # 更改params中的max参数
            params['max'] = last_pin_id
            # 再次请求
            z = requests.get(url=hburl, params=params, headers=heads)
            # 清空数组
            list_keys = []
            # 再次获取相应的参数
            for x in z.json()['pins']:
                list_keys.append((x['file']).get('key'))
            download(list_keys)
        except:
            break


# 下载到本地的函数
def download(arr):
    for i in arr:
        # 拼接成完整地址
        imgurl = 'http://img.hb.aicdn.com/' + i
        print(imgurl)
        # 通过urllib读取地址内容
        img = urllib.request.urlopen(imgurl).read()
        # 拼接图片名字，包括格式
        file_name = imgurl.split('/')[-1].replace('20%', '') + '.jpg'
        # open函数会打开指定路径，存在该文件则打开，不存在则创建后再打开
        file = open("/home/wangxy/Desktop/古装美女" + '/' + file_name, 'wb')
        # 将图片信息写入到本地
        file.write(img)
        # 关闭资源
        file.close()


# 主函数
if __name__ == '__main__':
    getpins()



