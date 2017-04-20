import requests

# 这里的headers就是网页中的headers，F12查看DOC
requests_headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '',
    'Host': 'www.zhihu.com',
    'Referer': 'https://zhuanlan.zhihu.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

# 请求的url,同上可得
url = "https://www.zhihu.com/people/excited-vczh/activities"

# 请求得请求方法，同上可得
z = requests.get(url, headers=requests_headers)
print(z.content)