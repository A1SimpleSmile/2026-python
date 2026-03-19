# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

"""
重點說明：
  帶星號的變數（*var）永遠接收「剩餘的零個或多個」元素，
  結果固定是 list（即使剩餘元素為零也是空 list，不是 None）。
  這讓解包程式碼能彈性應對元素數量不固定的資料。
"""

# ── 情況一：剩餘元素為「空」，phones 仍是空 list ─────────────────────
record_no_phone = ("Dave", "dave@example.com")
name, email, *phones = record_no_phone

print("=== 沒有電話號碼 ===")
print(f"name   = {name}")
print(f"email  = {email}")
print(f"phones = {phones}")          # []，是 list 而非 None
print(f"type   = {type(phones)}")    # <class 'list'>

# ── 情況二：剩餘元素有多筆 ───────────────────────────────────────────
record_multi = ("Dave", "dave@example.com", "555-1234", "555-5678")
name, email, *phones = record_multi

print("\n=== 有多筆電話號碼 ===")
print(f"name   = {name}")
print(f"email  = {email}")
print(f"phones = {phones}")          # ['555-1234', '555-5678']

# ── 情況三：星號可以放在「中間」或「開頭」 ───────────────────────────
first, *middle, last = [1, 2, 3, 4, 5]
print("\n=== 星號放中間 ===")
print(f"first  = {first}")
print(f"middle = {middle}")          # [2, 3, 4]
print(f"last   = {last}")

*head, second_last, last = range(1, 6)
print("\n=== 星號放開頭 ===")
print(f"head        = {head}")
print(f"second_last = {second_last}")
print(f"last        = {last}")

# ── 情況四：為何結果一定是 list？ ───────────────────────────────────
# Python 語言規範保證星號解包的結果永遠是 list，
# 方便後續直接呼叫 .append()、切片等 list 專屬操作。
print("\n=== 型別驗證 ===")
print(isinstance(phones, list))      # True
print(isinstance(middle, list))      # True

