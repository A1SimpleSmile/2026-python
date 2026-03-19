# U10. zip 為何只能用一次（1.8）

"""
重點說明：
  zip() 回傳的是一個「惰性迭代器（lazy iterator）」，不是 list。
  迭代器只能從頭到尾走一次，被全部消耗後就空了，
  第二次迭說會得到空結果而不換出錯誤（這是常見降阱）。
  解決方法：如果需要多次使用，用 list(zip(...)) 先存成序列。
"""

prices = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "FB": 10.75}

# ── 示範一：zip 迭代器第二次使用會得到空結果 ────────────────────────────
# 建立一次 zip 迭代器
z = zip(prices.values(), prices.keys())

print("=== zip 迭代器只能用一次 ===")
result_min = min(z)   # 消耗掉迭代器，得到 (value, key) 的最小對
print(f"min(z) = {result_min}")

# z 已被全部消耗，再一次 max(z) 不會拋出錯誤，只會回傳 「空迭代器的預設值」
result_max = max(z, default=None)   # 加 default 避免 ValueError
print(f"max(z) 再次呼叫 = {result_max}")   # None，迭代器已空

# ── 示範二：用 list() 存起來再多次使用 ──────────────────────────────────
z_list = list(zip(prices.values(), prices.keys()))   # 立即轉成 list 存起
print("\n=== 先轉成 list 再多次使用 ===")
print(f"z_list = {z_list}")
print(f"min    = {min(z_list)}")   # 正常
print(f"max    = {max(z_list)}")   # 正常，list 不會被消耗

# ── 示範三：所有內建迭代器都有相同問題 ────────────────────────────────
# map()、filter()、enumerate()、generator expression 都是惰性迭代器，迭說一次就空了。
print("\n=== 其他迭代器同樣只能用一次 ===")
gen = (x * 2 for x in range(5))    # 生成器表達式
print(f"sum(gen) = {sum(gen)}")     # 0+2+4+6+8 = 20
print(f"再迭說：{list(gen)}")      # []，已被消耗

# ── 小結：迭代器 vs. 可迭代物件（iterable）的差異 ────────────────────────
# list、tuple、dict 是「可迭代物件」，可重複迭說。
# zip()、map()、filter()、generator 是「迭代器」，只能走一次。
my_list = [1, 2, 3]
print("\n=== list 可重複迭說 ===")
print(f"第一次：{list(my_list)}")
print(f"第二次：{list(my_list)}")   # 仍有資料

