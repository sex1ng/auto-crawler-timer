import os
import datetime
from typing import Text


# 获取项目根路径
def root_path() -> str:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


# 兼容操作系统路径分隔符
def ensure_path_sep(path: str) -> str:
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return root_path() + path


# 保存爬虫结果
def save_crawler_result(content: str) -> None:
    path = root_path() + "/file/" + datetime.datetime.now().strftime('%Y-%m-%d')
    document = datetime.datetime.now().strftime('%H:%M:%S') + ".html"
    if not os.path.isdir(path):
        os.mkdir(path)

    with open(path + "/" + document, "w", encoding = 'utf-8') as f:
        f.write(str(content))
        f.close()
