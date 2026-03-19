# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

"""
重點說明：
  Python 3.7+ 起，內建 dict 已保證「插入順序」，
  所以一般情況下不再需要 OrderedDict。
  但 OrderedDict 仍有兩個普通 dict 沒有的獨特能力：
    1. move_to_end(key)   ── 把某個 key 移到最前或最後，O(1)。
    2. popitem(last=...)  ── 依照 LIFO（last=True）或 FIFO（last=False）彈出。
  代價：底層多維護一條雙向鏈結串列（doubly linked list）來記錄順序，
        因此每個 entry 比普通 dict 多佔用約 2 個指標的記憶體。
"""

import sys
from collections import OrderedDict

# ── 示範一：插入順序保留 ────────────────────────────────────────────
d = OrderedDict()
d["foo"] = 1
d["bar"] = 2
d["baz"] = 3

print("=== 插入順序 ===")
for k, v in d.items():
    print(f"  {k}: {v}")   # 永遠以 foo → bar → baz 順序輸出

# ── 示範二：move_to_end（普通 dict 做不到）──────────────────────────
# last=True（預設）→ 移到最後；last=False → 移到最前。
d.move_to_end("foo")          # 把 "foo" 移到串列尾端
print("\n=== move_to_end('foo') → 移到尾端 ===")
print(list(d.keys()))         # ['bar', 'baz', 'foo']

d.move_to_end("foo", last=False)   # 把 "foo" 移回最前端
print("move_to_end('foo', last=False) → 移到前端")
print(list(d.keys()))         # ['foo', 'bar', 'baz']

# ── 示範三：popitem 依順序彈出 ──────────────────────────────────────
d2 = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

# last=True（預設）→ LIFO，從尾端彈出（Stack 行為）
k, v = d2.popitem(last=True)
print(f"\n=== popitem(last=True)  → LIFO ===")
print(f"彈出：{k}={v}，剩餘：{list(d2.keys())}")   # 彈出 c

# last=False → FIFO，從頭端彈出（Queue 行為）
k, v = d2.popitem(last=False)
print(f"popitem(last=False) → FIFO")
print(f"彈出：{k}={v}，剩餘：{list(d2.keys())}")   # 彈出 a

# ── 示範四：相等性比較會考慮順序（普通 dict 不在乎順序）────────────
od1 = OrderedDict([("x", 1), ("y", 2)])
od2 = OrderedDict([("y", 2), ("x", 1)])
rd1 = {"x": 1, "y": 2}
rd2 = {"y": 2, "x": 1}

print("\n=== 相等性比較 ===")
print(f"OrderedDict 順序不同：{od1 == od2}")   # False，順序不同就不相等
print(f"普通 dict   順序不同：{rd1 == rd2}")   # True，普通 dict 不在乎順序

# ── 示範五：記憶體佔用對比 ──────────────────────────────────────────
# OrderedDict 底層多一條雙向鏈結串列，每個 entry 多兩個指標欄位，
# 在大量 key 時記憶體差異會顯著。
n = 1000
plain = {i: i for i in range(n)}
ordered = OrderedDict((i, i) for i in range(n))

print("\n=== 記憶體佔用（sys.getsizeof，僅計外殼）===")
print(f"  dict         : {sys.getsizeof(plain):>8} bytes")
print(f"  OrderedDict  : {sys.getsizeof(ordered):>8} bytes")
print("  （OrderedDict 外殼更大，實際差異含內部鏈結節點會更多）")

# ── 結論 ─────────────────────────────────────────────────────────────
print("""
結論：
  ✓ 只需保留插入順序          → 用普通 dict（Python 3.7+）即可
  ✓ 需要 move_to_end / FIFO popitem → 才值得用 OrderedDict
  ✓ 需要「相等性比較含順序」  → 使用 OrderedDict
""")

