import sys
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(ROOT_DIR)

print(ROOT_DIR)

sys.exit()

from app.common import *


options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
chromedriver_path = '/bin/chromedriver'
driver = webdriver.Chrome(executable_path = chromedriver_path, chrome_options = options)

keyword = "%E7%BE%8E%E5%A5%B3"
url = f"https://www.zhihu.com/search?type=content&q={keyword}"

driver.get(url)
driver.implicitly_wait(10)

html = driver.page_source

# save_crawler_result(html)

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
'''
//*[@id="SearchMain"]/div/div/div/div/div[3]/div/div/div/h2/span/div/a/@href
//*[@id="SearchMain"]/div/div/div/div/div[4]/div/div/div/h2/span/div/a/@href
//*[@id="SearchMain"]/div/div/div/div/div[5]/div/div/div/h2/span/div/a/@href
:Authority:
www.zhihu.com
:Method:
GET
:Path:
/api/v3/oauth/sms/supported_countries
:Scheme:
https
Accept:
*/*
Accept-Encoding:
gzip, deflate, br
Accept-Language:
zh,en;q=0.9,zh-CN;q=0.8
Cookie:
_zap=d8fc560a-0764-4451-a661-22a4d667f5ed; _xsrf=93eea651-ce85-42e1-a7cd-0f7a581145e6; d_c0=ADAWNz6K5xaPTlNlmoU-SRyhBE1DhsdqIPE=|1686275509; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1686275508; SESSIONID=UUC2sinqBuDomOk9hKycgM6o53Vn8bq7BzT2xfafObh; JOID=W1wVBUqpWfc5898SQaZs58_MWvBe8QiyDIi7eDbjIbdQmZh0fBXedFL21hBA0sk5kDAFKyJufVDILN62snysdFk=; osd=W1ETAk2pVPE-9N8fR6Fr58LKXfde_A61C4i2fjHkIbpWnp90cRPZc1L70BdH0sQ_lzcFJiRpelDFKtmxsnGqc14=; YD00517437729195%3AWM_NI=02rzksQQanbAj97dr5Y6ZmzF50ztXqnawhVHlEXUs1TJhXk3f3tnwnE8JxShV2VA6R8OXlH8rE8kV%2FY%2B%2BNN7rn8YZcrgPArl%2FRx09SShw1RkXbrxE9WRrGqh%2FvggK%2B2Zb1U%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea5c780af8eacb5ef339cb48fb6d15e979a8bacd4688ebafd94aa3bb0bbffb4e82af0fea7c3b92af4eebe9bea79938faf8fe14baae7f985f13f9bea968ef94ef7f0b695db7baebfb989d544b09b98b6f23b9896a8b9ea39a6edbc8ff66687e88699d26496ee9aa2b55afc91988dcb34b29bf88cd5259bf5e5afcd3db2b2f8bad969b2b9a0a2f168ed8eb8d1bc5991b8b9d2d1619cbebe99c833958ebea8f464edaaa988ca21f286aed2d837e2a3; YD00517437729195%3AWM_TID=KZ7Wh4rlplxAEEQREBKRgYOn97w0OwWb; captcha_session_v2=2|1:0|10:1686277034|18:captcha_session_v2|88:Y2tuMjlMVzVPMTlTQzhybk9aMUtiNjJ1d0tiZHhXOTUzWjBXcCt2bjdra1Y0bUNFRDBlaHZQSkY5MXRPVXpUbA==|d635c974b6fa688f7b2a6298606438e3b8ad0e7e690a5141720c08cc044abdaf; gdxidpyhxdE=fHu0Qq2ljk%2FKlyZEhZQaGgjGGBHvtzgbAVV4ff69Q3vOqBgtrxQmR1Ta33g50rGbeQeif2heQSDlUYxOrzgsG7K9ovaIRXdqd%5C6DKnh%2F%2BXVlpCRQ41nadlJ7UOdLBTJIILzbw1Gzao8%2BcHguDA2VKg8myy7%2FebYgaN70Ln9iYkKd3H30%3A1686277933395; KLBRSID=b33d76655747159914ef8c32323d16fd|1686295811|1686289121; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1686295810
Referer:
https://www.zhihu.com/search?type=content&q=%E7%BE%8E%E5%A5%B3
Sec-Ch-Ua:
"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"
Sec-Ch-Ua-Mobile:
?0
Sec-Ch-Ua-Platform:
"Windows"
Sec-Fetch-Dest:
empty
Sec-Fetch-Mode:
cors
Sec-Fetch-Site:
same-origin
User-Agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
X-Ab-Param:
X-Ab-Pb:
CiAbAD8ARwC0AHQBOwLXAtgCtwPWBIsFjAUnB3QIhwv4DBIQAAAAAAAAAAAAAAAAAAAAAA==
X-Requested-With:
fetch
X-Zse-93:
101_3_3.0
X-Zse-96:
2.0_nw5zOazgInlIscCSGI7bl89Nx98zVP4grpQwIH/KAqr0Io3s6fztQjnJae4xDVwx
'''
