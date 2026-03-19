# U8. 字典最值為何常用 zip(values, keys)（1.8）

"""
重點說明：
  對字典直接呼叫 min(d) / max(d)，比較的是「鍵（key）」而非值（value）。
  若只用 min(d.values())，可以拿到最小值，但無法知道對應的鍵是哪個。
  解法：zip(d.values(), d.keys()) 把 (value, key) 配對成 tuple，
        min/max 會先比 tuple 第一個元素（value），相同才比第二個（key），
        因此一次就能同時拿到「最小值」與「對應的鍵」。
"""

prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM":  205.55,
    "HPQ":   37.20,
    "FB":   10.75,
}

# ── 示範一：min(d) 比較的是 key（字母序），不是 value ───────────────
min_key = min(prices)        # 等同 min(prices.keys())
max_key = max(prices)

print("=== min/max 直接對字典 → 比較 key（字母序）===")
print(f"min(prices) = {min_key}")   # 字母序最小的 key：'AAPL'
print(f"max(prices) = {max_key}")   # 字母序最大的 key：'IBM'

# ── 示範二：min(d.values()) 只拿到值，不知道對應 key ────────────────
min_val = min(prices.values())
max_val = max(prices.values())

print("\n=== min/max 對 .values() → 只有值，不知道是哪支股票 ===")
print(f"min(prices.values()) = {min_val}")   # 10.75，但不知道是 'FB'
print(f"max(prices.values()) = {max_val}")   # 612.78，但不知道是 'AAPL'

# ── 示範三：zip(values, keys) 同時取得值與鍵 ────────────────────────
# zip 把兩個序列逐一配對成 (value, key) 的 tuple。
# min/max 比較 tuple 時，先比第一欄（value），
# 若相同再比第二欄（key），因此能正確找出「最小值對應的 key」。
min_pair = min(zip(prices.values(), prices.keys()))
max_pair = max(zip(prices.values(), prices.keys()))

print("\n=== zip(values, keys) → 同時拿到值與鍵 ===")
print(f"min：值={min_pair[0]}, 股票={min_pair[1]}")   # (10.75, 'FB')
print(f"max：值={max_pair[0]}, 股票={max_pair[1]}")   # (612.78, 'AAPL')

# ── 示範四：等效寫法——用 key= 參數（可讀性更高）─────────────────────
# min(d, key=d.get) 讓 min 比較「每個 key 對應的 value」，
# 直接回傳「值最小的 key」，比 zip 寫法更直觀。
min_stock = min(prices, key=prices.get)
max_stock = max(prices, key=prices.get)

print("\n=== min(d, key=d.get) → 直接回傳對應的 key ===")
print(f"最低價股票：{min_stock}（${prices[min_stock]}）")
print(f"最高價股票：{max_stock}（${prices[max_stock]}）")

# ── 示範五：zip 方案在 value 相同時的平手處理 ────────────────────────
# 若兩個 value 相等，zip 方案會接著比較 key（字母序）決定勝負，
# 而 key= 方案則依遍歷順序取第一個（行為依實作而定）。
tie = {"X": 100.0, "A": 100.0, "M": 100.0}
print("\n=== value 相同時的平手比較 ===")
print(f"zip 方案 min：{min(zip(tie.values(), tie.keys()))}")   # (100.0, 'A')，字母序最小
print(f"key= 方案 min：{min(tie, key=tie.get)}")               # 第一個遇到的 key
