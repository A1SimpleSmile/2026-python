# R10. 去重且保序（1.10）

# 目標：移除重複元素，但保留第一次出現的順序。
def dedupe(items):
    # seen 用來記錄已看過的值。
    seen = set()
    for item in items:
        # 沒看過才輸出（yield）並記錄。
        if item not in seen:
            yield item
            seen.add(item)

# 進階版：可指定 key，把不可雜湊型態轉成可比較鍵值。
# 常用在 list[dict] 的去重。
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        # 有 key 函式時，用 key(item) 作為去重依據。
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
