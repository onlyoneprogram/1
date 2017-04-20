import requests


heads = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

url = "https://itunes.apple.com/cn/app/%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80/id989673964"

z = requests.get(url=url, headers=heads)

print(z.status_code)
print(z.headers)
last_modified = z.headers['Last-Modified']
print(last_modified)
heads['If-Modified-Since'] = last_modified
z1 = requests.get(url=url, headers=heads)
print(z1.status_code)