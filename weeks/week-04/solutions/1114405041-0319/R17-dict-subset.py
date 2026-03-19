# R17. 字典子集（1.17）

"""
重點說明：
字典推導式（dict comprehension）寫法為 {k: v for k, v in d.items() if 條件}，
可以快速從一個大字典篩選出符合條件的子字典（subset），
比事先建立空字典再逐筆塞入來得更簡潔易讀。
"""

# 股票名稱 → 股價的字典（模擬原始資料）
prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM":  205.55,
    "HPQ":   37.20,
    "FB":   10.75,
}

print("原始字典：", prices)

# ── 篩選方式一：依「值」篩選 ──────────────────────────────
# 只保留股價 > 200 的項目。
# .items() 同時拿到 key（k）和 value（v），在 if 後面判斷 v 的條件。
p1 = {k: v for k, v in prices.items() if v > 200}
print("\n股價 > 200 的子字典（依值篩選）：", p1)

# ── 篩選方式二：依「鍵」篩選 ──────────────────────────────
# 只保留鍵存在於指定集合（set）中的項目。
# 用集合（set）做成員判斷的時間複雜度是 O(1)，比用 list 快。
tech_names = {"AAPL", "IBM"}
p2 = {k: v for k, v in prices.items() if k in tech_names}
print("科技股子字典（依鍵篩選）：       ", p2)

# ── 補充：同時對值做轉換 ─────────────────────────────────
# 字典推導式的 v 部分也可以做運算，例如把股價乘以 10 換算成便士（pence）。
p3 = {k: round(v * 10, 2) for k, v in prices.items() if v > 200}
print("\n股價 > 200 的項目（轉換成便士）：", p3)

