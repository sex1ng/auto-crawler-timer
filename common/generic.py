import os


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
    import datetime

    path = root_path() + "/file/" + datetime.datetime.now().strftime('%Y-%m-%d')
    document = datetime.datetime.now().strftime('%H-%M-%S') + ".html"

    if not os.path.isdir(path):
        os.mkdir(path)

    with open(path + "/" + document, "w", encoding='utf-8') as f:
        f.write(str(content))
        f.close()


# 读取 yaml 文件
def read_yaml(key=None):
    import yaml

    with open(root_path() + '/common/config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    if key is None:
        return config
    else:
        return config[key]


# 读取 json 文件
def read_json(key=None):
    import json

    with open(root_path() + '/common/config.json', 'r') as f:
        config = json.load(f)

    if key is None:
        return config
    else:
        return config.get(key)


# 读取 xml 文件
def read_xml(key: str) -> str:
    import xml.dom.minidom

    dom = xml.dom.minidom.parse(root_path() + '/common/config.xml')
    value = dom.getElementsByTagName(key)[0].childNodes[0].data

    return value


# 解析 html 文件
def read_html(path: str, parsing=True) -> str:
    from lxml import html

    with open(path, 'r') as file:
        content = file.read()

    if not parsing:
        return content

    parsed_content = html.fromstring(content)

    return parsed_content
