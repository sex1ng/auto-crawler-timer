import os
import sys
import requests
import re

session = requests.session()
index_url = 'https://www.zhihu.com'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

def get_xsrf():
    index_page = session.get(index_url)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    _xsrf = re.findall(pattern, html)

    return _xsrf

print(get_xsrf())
