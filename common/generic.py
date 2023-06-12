import os
import datetime
from typing import Text


def root_path():
    """ 获取 根路径 """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


def ensure_path_sep(path: Text) -> Text:
    """ 兼容 windows 和 linux 不同环境的操作系统路径 """
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return root_path() + path


def save_crawler_result(content):
    """ 写入文件 """
    resources_path = "/data/python/resources/" + datetime.datetime.now().strftime('%Y-%m-%d')
    resources_file = datetime.datetime.now().strftime('%H-%i-%s') + ".html"
    if not os.path.isdir(resources_path):
        os.mkdir(resources_path)

    with open(resources_path + "/" + resources_file, "w", encoding = 'utf-8') as f:
        f.write(str(content))
        f.close()
