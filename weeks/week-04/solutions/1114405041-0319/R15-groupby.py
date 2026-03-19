# R15. 分組 groupby（1.15）

"""
重點說明：
1. itertools.groupby 只會把「連續且鍵值相同」的資料分在同一組。
2. 因此在 groupby 前，通常需要先依同一個 key 排序，否則同日期資料可能被拆成多組。
"""

from itertools import groupby
from operator import itemgetter

# 模擬「已經讀進來但尚未整理」的交易/地址資料
# 注意：同一個 date 可能出現多筆，且原始順序不一定已排序。
rows = [
    {"date": "07/01/2012", "address": "5412 N CLARK"},
    {"date": "07/04/2012", "address": "5148 N CLARK"},
    {"date": "07/01/2012", "address": "5800 E 58TH"},
    {"date": "07/03/2012", "address": "2122 N CLARK"},
    {"date": "07/02/2012", "address": "5645 N RAVENSWOOD"},
    {"date": "07/03/2012", "address": "1060 W ADDISON"},
    {"date": "07/02/2012", "address": "4801 N BROADWAY"},
    {"date": "07/01/2012", "address": "1039 W GRANVILLE"},
]

# 先依 date 排序，確保同日期資料會連在一起。
rows.sort(key=itemgetter("date"))

print("=== 依日期分組後的資料 ===")

# groupby 會回傳 (鍵值, 該組迭代器)
# 鍵值由 key=itemgetter("date") 決定，也就是每筆字典的 date 欄位。
for date, items in groupby(rows, key=itemgetter("date")):
    print(f"\n日期：{date}")

    # items 是「一次性迭代器」，通常會在這裡立即走訪或轉成 list。
    for item in items:
        print(f"  - {item['address']}")
