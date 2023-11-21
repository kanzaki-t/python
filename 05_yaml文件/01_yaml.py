"""
yaml文件是用来方便读写得一种格式
    大小写敏感
    缩进表示层级关系
    缩进时不允许使用tab，仅允许使用空格
    空格的多少不重要，关键是相同层级的元素要对齐
    #表示注释
"""

import yaml

f = open("config.yml", "r", encoding="utf=8")
conf_str = f.read()
f.close()
data = yaml.safe_load(conf_str)
print(data)
# data就是键值对形式的字典
# {'id': 'nadia', 'password': 123}
