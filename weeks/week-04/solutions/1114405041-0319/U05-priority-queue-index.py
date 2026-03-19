# U5. 優先佇列為何要加 index（1.5）

"""
重點說明：
  heapq 在比較元素時，若 tuple 的第一個欄位（priority）相同，
  會繼續比較第二個欄位。
  若第二個欄位是自訂物件且沒有定義 __lt__，Python 就會拋出 TypeError。

  解決方法：在 (priority, item) 之間插入一個「遞增計數器 index」，
  讓 heap 永遠不需要比較到物件本身：
    (priority, index, item)
    ↑ 主排序    ↑ 次排序（整數一定可比較）   ↑ 不會被比較到

  結果：相同 priority 的元素依「插入順序」（FIFO）排序。
"""

import heapq

class Item:
    """自訂物件，刻意不定義 __lt__，模擬無法比較的情況。"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item({self.name!r})"

# ── 示範一：只放 (priority, item) 會 TypeError ───────────────────────
print("=== 沒有 index，同 priority 會 TypeError ===")
pq_bad = []
heapq.heappush(pq_bad, (1, Item("a")))
try:
    heapq.heappush(pq_bad, (1, Item("b")))   # 第一欄位相同 → 嘗試比較 Item → 炸
except TypeError as e:
    print(f"錯誤：{e}")
    print("原因：priority 相同時 heap 嘗試比較 Item 物件，但 Item 沒有定義 __lt__。")

# ── 示範二：加入 index 作為中間層 ───────────────────────────────────
print("\n=== 加入 index 後正確運作 ===")
pq = []
idx = 0   # 單調遞增計數器，確保每個 index 都唯一

tasks = [
    (2, Item("低優先度 A")),
    (1, Item("高優先度")),
    (2, Item("低優先度 B")),   # 與第一筆 priority 相同
    (3, Item("最低優先度")),
]

for priority, item in tasks:
    # tuple 結構：(priority, index, item)
    # priority  → 主要排序依據（數字小 = 優先度高）
    # index     → 次要排序依據（整數可直接比較，避免觸碰 item）
    # item      → 實際工作物件（不參與排序）
    heapq.heappush(pq, (priority, idx, item))
    idx += 1

print("依優先度（小 → 大）逐一 pop：")
while pq:
    p, i, task = heapq.heappop(pq)
    print(f"  priority={p}, index={i}, task={task}")
    # 相同 priority（2）的兩個 Item 依 index（插入順序，FIFO）排序。

# ── 示範三：以 負數 priority 模擬「最大堆積（max-heap）」──────────────
# Python heapq 只有 min-heap；若想讓「數值大的優先度高」，
# 存入時把 priority 取負號，pop 時再取負號還原。
print("\n=== 負數 priority 模擬 max-heap ===")
pq_max = []
for p, item in [(1, "低"), (5, "高"), (3, "中")]:
    heapq.heappush(pq_max, (-p, item))   # 存入負號
while pq_max:
    neg_p, item = heapq.heappop(pq_max)
    print(f"  priority={-neg_p}（還原）, item={item}")

