import sys
import os
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree

from common.generic import *

user_agent_tuple = (
    # Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    # Edge
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
    # Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    # Safari
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
)

options = Options()
options.add_argument('--no-sandbox')  # 禁用沙盒模式(解决DevToolsActivePort文件不存在的报错)。
options.add_argument('--headless')  # 无界面模式。
options.add_argument('--disable-gpu')  # 禁用 GPU 加速。
options.add_argument('--disable-extensions')  # 禁用扩展。
options.add_argument('window-size=1920x1080')  # 设置窗口大小。
options.add_argument('--disable-dev-shm-usage')  # 禁用 /dev/shm。
options.add_argument('--disable-blink-features=AutomationControlled')  # 禁用自动化。
options.add_argument('--disable-blink-features=AutomationControlled')  # 去除 webdriver 痕迹。
options.add_argument('--disable-blink-features=BlockCredentialedSubresources')  # 禁用阻止凭据资源的功能。
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 禁用自动化扩展插件。
options.add_experimental_option('useAutomationExtension', False)  # 隐藏被浏览器被自动化工具控制横幅。

UserAgent = random.choice(user_agent_tuple)
options.add_argument(f'--user-agent={UserAgent}')  # 设置 User-Agent

chromedriver_path = '/bin/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=options)

keyword = "%E7%BE%8E%E5%A5%B3"
url = f"https://www.zhihu.com/search?type=content&q={keyword}"

driver.get(url)
driver.implicitly_wait(10)

html = driver.page_source

save_crawler_result(html)

driver.quit()

sys.exit()

tree = etree.HTML(html)
# links = tree.xpath('//*[@id="SearchMain"]/div/div/div/div/div[position()>2]//a[@class="Link--primary"]/@href')
# links = tree.xpath('//*[@id="SearchMain"]/div/div/div/div/div[3]/div/div/div/h2/span/div/a/@href')
links = tree.xpath('//*[@id="SearchMain"]')

print(links)

# etree.tostring(ex).decode()

for link in links:
    print(link)

driver.quit()

sys.exit()
