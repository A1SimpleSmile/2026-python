# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）

"""
重點說明：
  直接解包（x, y, z = ...）時，左側變數數量必須與右側元素數量完全一致，
  否則 Python 會拋出 ValueError。
  解決方法：
    1. 調整變數數量符合元素數量。
    2. 若元素數量不固定，改用「星號解包」(starred unpacking) 吸收多餘元素。
"""

# ── 示範一：正常解包 ────────────────────────────────────────────────
p = (4, 5)
x, y = p          # 變數 2 個、元素 2 個 → 完全符合
print("=== 正常解包 ===")
print(f"x={x}, y={y}")

# ── 示範二：主動觸發 ValueError，並用 try/except 捕捉 ───────────────
print("\n=== 解包數量不符（ValueError）===")
try:
    x, y, z = p   # 元素只有 2 個，但變數要 3 個 → ValueError
except ValueError as e:
    print(f"錯誤：{e}")
    print("原因：左側變數 3 個，右側元素只有 2 個，數量不符。")

# ── 示範三：元素太多也會失敗 ────────────────────────────────────────
q = (1, 2, 3, 4)
print("\n=== 元素過多也會失敗 ===")
try:
    a, b = q      # 元素 4 個，變數 2 個 → 同樣 ValueError
except ValueError as e:
    print(f"錯誤：{e}")

# ── 示範四：用星號解包解決「數量不確定」的情況 ──────────────────────
# 星號變數會把「剩餘所有元素」打包成 list，讓左側變數數量可以少於右側元素數量。
record = ("Dave", 40, "dave@example.com", "123-456", "789-012")
name, age, email, *phones = record

print("\n=== 星號解包（數量不固定的解法）===")
print(f"name  = {name}")
print(f"age   = {age}")
print(f"email = {email}")
print(f"phones = {phones}")   # ['123-456', '789-012']，永遠是 list

