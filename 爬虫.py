#encoding:utf-8

import requests
import json

url = 'http://raspberry.fourbrother666.cn/php/public/index.php/api/music/getMusicList'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'content-type': 'application/json'
}
proxies = {  # 代理 ip,内网可直接使用
    'http': 'http://127.0.0.1:12639',
    'https': 'https://127.0.0.1:12639'
}
r = requests.get(url, proxies=proxies, headers=headers, allow_redirects=True)
content = r.text
if content.startswith(u'\ufeff'):
        content = content.encode('utf8')[3:].decode('utf8')
print(json.loads(content)[0])