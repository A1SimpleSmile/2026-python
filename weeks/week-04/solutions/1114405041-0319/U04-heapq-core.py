# U4. heap 為何能高效拿 Top-N（1.4）

"""
重點說明：
  Python 的 heapq 模組實作「最小堆積（min-heap）」：
    - heapify(h)    ：把任意 list 原地重新排列成 heap，O(N)。
    - h[0]          ：永遠是目前最小值（heap 核心性質），O(1) 查看。
    - heappop(h)    ：取出並移除最小值，O(log N)。
    - heappush(h, v)：加入新元素並維持 heap 性質，O(log N)。
  Top-N 效率優勢：
    - 若只需最小/最大的 N 個元素（N << 總長度），
      heapq.nsmallest / nlargest 使用 heap 比全排序 O(N log N) 更快。
"""

import heapq

# ── 示範一：heapify 與 h[0] ──────────────────────────────────────────
nums = [5, 1, 9, 2, 7, 3]
h = nums[:]           # 複製一份，避免修改原串列
heapq.heapify(h)      # 原地重排為 min-heap，不一定完全排序，但 h[0] 一定最小

print("=== heapify ===")
print(f"原始串列：{nums}")
print(f"heap 結構：{h}")
print(f"h[0]（最小值）= {h[0]}")

# ── 示範二：逐步 heappop，每次都能拿到目前最小 ──────────────────────
print("\n=== 逐步 heappop ===")
temp = h[:]
while temp:
    m = heapq.heappop(temp)   # O(log N)，取出最小值並維持 heap
    print(f"pop → {m}，剩餘 heap：{temp}")
# 觀察：pop 出的順序就是遞增排序

# ── 示範三：heappush 動態加入元素 ───────────────────────────────────
print("\n=== heappush ===")
h2 = []
for v in [4, 8, 1, 6, 2]:
    heapq.heappush(h2, v)
    print(f"push({v}) → heap={h2}，目前最小={h2[0]}")

# ── 示範四：nsmallest / nlargest（Top-N 的主角）────────────────────
scores = [88, 72, 95, 63, 99, 81, 57, 76]
print("\n=== nsmallest / nlargest ===")
print(f"所有成績：{scores}")
print(f"最低 3 名：{heapq.nsmallest(3, scores)}")
print(f"最高 3 名：{heapq.nlargest(3, scores)}")

# ── 示範五：對字典串列用 key 取 Top-N ───────────────────────────────
portfolio = [
    {"name": "IBM",  "shares": 100, "price": 91.1},
    {"name": "AAPL", "shares":  50, "price": 543.22},
    {"name": "FB",   "shares": 200, "price":  21.09},
    {"name": "HPQ",  "shares":  35, "price":  31.75},
]
cheapest2 = heapq.nsmallest(2, portfolio, key=lambda s: s["price"])
print("\n=== 最便宜的 2 支股票 ===")
for s in cheapest2:
    print(f"  {s['name']}: ${s['price']}")

