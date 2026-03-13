# R13. 字典列表排序 itemgetter（1.13）

# itemgetter 可快速取 dict 某些欄位，常用於 sorted 的 key。
from operator import itemgetter

# 每個元素都是 dict（姓名 + uid）。
rows = [{'fname': 'Brian', 'uid': 1003}, {'fname': 'John', 'uid': 1001}]

# 依名字排序。
sorted(rows, key=itemgetter('fname'))

# 依 uid 排序。
sorted(rows, key=itemgetter('uid'))

# 依多欄位排序：先 uid，再 fname。
sorted(rows, key=itemgetter('uid', 'fname'))
