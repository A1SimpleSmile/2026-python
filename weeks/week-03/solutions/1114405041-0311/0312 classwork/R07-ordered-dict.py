# R7. OrderedDict（1.7）

# OrderedDict 會記住 key 的插入順序。
from collections import OrderedDict
import json

d = OrderedDict()

# 插入順序是 foo -> bar。
d['foo'] = 1; d['bar'] = 2

# 轉成 JSON 時會依插入順序輸出。
json.dumps(d)
