# R19. 轉換+聚合：生成器表達式（1.19）

"""
重點說明：
生成器表達式（generator expression）可以直接作為 sum()、min()、max()、
any()、all() 等聚合函式的引數，不需要先建立中間的 list，
節省記憶體（尤其在資料量大時效益顯著）。
語法：func(運算式 for 變數 in 可迭代物件 if 條件)
"""

# ── 範例一：sum + 生成器（平方和） ─────────────────────────────
# 不用先建 [1, 4, 9]，生成器會逐筆把 x*x 餵給 sum()。
nums = [1, 2, 3, 4, 5]
total = sum(x * x for x in nums)
print("=== sum + 生成器 ===")
print("原始數列：", nums)
print("平方和：  ", total)   # 1 + 4 + 9 + 16 + 25 = 55

# ── 範例二：join + 生成器（混合型別 tuple 轉字串） ──────────────
# tuple 中同時有字串和數字，str(x) 先個別轉成字串再串接。
s = ("ACME", 50, 123.45)
joined = ",".join(str(x) for x in s)
print("\n=== join + 生成器 ===")
print("原始 tuple：", s)
print("串接結果：  ", joined)

# ── 範例三：min/max + 生成器（對字典串列聚合） ──────────────────
portfolio = [
    {"name": "AOL",  "shares": 20},
    {"name": "YHOO", "shares": 75},
    {"name": "IBM",  "shares": 45},
    {"name": "AAPL", "shares": 10},
]

# 方法 A：只取出 shares 的最小值（單純數字）。
min_shares = min(s["shares"] for s in portfolio)
print("\n=== min + 生成器 ===")
print("最少持股數：", min_shares)

# 方法 B：用 key= 取得「持股最少的完整字典」，保留完整資訊。
# lambda 告訴 min() 用哪個欄位比較，回傳的是整個字典物件。
min_item = min(portfolio, key=lambda s: s["shares"])
print("持股最少的項目：", min_item)

# ── 補充：any / all + 生成器 ────────────────────────────────────
# any()：只要有一個元素符合條件就回傳 True。
# all()：所有元素都符合條件才回傳 True。
has_large = any(s["shares"] > 50 for s in portfolio)
all_positive = all(s["shares"] > 0 for s in portfolio)
print("\n=== any / all ===")
print("有持股 > 50 嗎？", has_large)
print("所有持股都 > 0？", all_positive)

