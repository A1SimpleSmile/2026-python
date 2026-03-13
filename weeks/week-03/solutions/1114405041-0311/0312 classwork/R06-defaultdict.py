# R6. 多值字典 defaultdict / setdefault（1.6）

# `defaultdict` 可以在 key 不存在時自動建立預設值。
from collections import defaultdict

# 這裡預設值工廠是 list。
# 第一次存取 d['a'] 時會自動建立 []。
d = defaultdict(list)
d['a'].append(1); d['a'].append(2)

# 換成 set 後，適合做「去重」收集。
d = defaultdict(set)
d['a'].add(1); d['a'].add(2)

# 不用 defaultdict 的對應寫法是 setdefault：
# 若 key 不存在，就先放入預設值（這裡是 []）。
d = {}
d.setdefault('a', []).append(1)
