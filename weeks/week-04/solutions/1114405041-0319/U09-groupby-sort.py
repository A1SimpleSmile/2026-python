# U9. groupby 為何一定要先 sort（1.15）

"""
重點說明：
  itertools.groupby 只會把「連續且鍵値相同」的元素放在同一組。
  若同一個日期的資料不連續，就會被分裂成多組，導致統計出錯。
  正確流程：先依分組用的同一欄位排序，再加上 groupby。
"""

from itertools import groupby
from operator import itemgetter

rows = [
    {"date": "07/02/2012", "x": 1},
    {"date": "07/01/2012", "x": 2},
    {"date": "07/02/2012", "x": 3},   # 07/02 被 07/01 隔開，不連續
]

# ── 示範一：沒有先排序，同一日期會被分裂 ───────────────────────────
print("=== 沒有先排序（错誤示範）===")
for date, items in groupby(rows, key=itemgetter("date")):
    group = list(items)   # 必須立即轉成 list，否則迭代器會被消耗
    print(f"  date={date}, 筆數={len(group)}, x値={[r['x'] for r in group]}")
# 預期結果：07/02 被分成兩組（分別包含 x=1 和 x=3），統計會出錯

print("  ↑ 07/02 被分裂成兩組！原因：groupby 只看「連續」相同的元素")

# ── 示範二：先排序，再 groupby ──────────────────────────────────────────
rows.sort(key=itemgetter("date"))   # 依 date 排序，相同日期的資料才會連在一起

print("\n=== 先排序後再 groupby（正確版）===")
for date, items in groupby(rows, key=itemgetter("date")):
    group = list(items)
    print(f"  date={date}, 筆數={len(group)}, x値={[r['x'] for r in group]}")
# 預期結果：07/01 一組（07/02 一組，分組正確

# ── 示範三：items 迭代器必須在迭說內用完，不能存起來後用 ───────────────
print("\n=== 迭代器就地消耗陷阱 ===")
rows2 = [
    {"dept": "RD", "name": "Alice"},
    {"dept": "RD", "name": "Bob"},
    {"dept": "HR", "name": "Carol"},
]
rows2.sort(key=itemgetter("dept"))

groups_saved = {}   # 假設先存迭說器再用

for dept, items in groupby(rows2, key=itemgetter("dept")):
    groups_saved[dept] = items  # 錯誤！儲存的是迭代器物件，不是資料

print("錯誤實作（存迭代器）:")
for dept, it in groups_saved.items():
    print(f"  {dept}: {list(it)}")   # 迭說器已被消耗，會得到空 list

# 正確做法：在迭說內立即轉成 list
groups_correct = {}
for dept, items in groupby(rows2, key=itemgetter("dept")):
    groups_correct[dept] = list(items)  # 立即轉成 list 才安全

print("正確實作（立即轉 list）:")
for dept, members in groups_correct.items():
    print(f"  {dept}: {[m['name'] for m in members]}")

