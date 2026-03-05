# 9 比較、排序與 key 函式範例
# ===========================================
# 本文件演示元組比較、排序函式以及使用lambda函式作為key參數

# ◆ 範例1：元組的比較運算
# 元組比較規則：從左到右逐一比較元素，直到找到不相等的為止
print("--- 元組比較 ---")
a = (1, 2)
b = (1, 3)

# 比較邏輯：
# 1. 先比較第一個元素：1 == 1，相等，繼續
# 2. 再比較第二個元素：2 < 3，所以 a < b 為 True
result = a < b
print(f"{a} < {b} = {result}")  # True

# 更多元組比較的例子
print(f"(1, 5) < (1, 3) = {(1, 5) < (1, 3)}")  # False
print(f"(1, 2, 3) < (1, 2, 4) = {(1, 2, 3) < (1, 2, 4)}")  # True

# ◆ 範例2：使用 key 參數排序複雜資料
# key 參數的作用：指定按什麼標準進行排序，而不是直接比較整個物件
print("\n--- 排序字典列表 ---")

rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
print(f"原始數據：{rows}")

# lambda r: r['uid'] 是一個匿名函式
# 作用：對每個字典r，提取其'uid'的值作為排序的鑰匙
# sorted() 會根據這些uid值(3, 1, 2)進行排序
rows_sorted = sorted(rows, key=lambda r: r['uid'], reverse=False)  # reverse=False表示升序
print(f"按uid排序後：{rows_sorted}")  # [{'uid': 1}, {'uid': 2}, {'uid': 3}]

# ◆ 範例3：在 min/max 中使用 key
# 默認情況下，min/max 直接比較物件，對於字典會報錯
# 使用key參數可以指定比較標準
print("\n--- 尋找最小值 ---")

# 找uid最小的字典
smallest = min(rows, key=lambda r: r['uid'])
print(f"uid最小的項目：{smallest}")  # {'uid': 1}

# 找uid最大的字典
largest = max(rows, key=lambda r: r['uid'])
print(f"uid最大的項目：{largest}")  # {'uid': 3}

# ◆ 進階示例：複雜的排序場景
print("\n--- 進階排序 ---")

# 假設有學生資料（姓名、分數、年級）
students = [
    {'name': '小王', 'score': 85, 'grade': 2},
    {'name': '小方', 'score': 90, 'grade': 1},
    {'name': '小李', 'score': 85, 'grade': 1},
]

# 按分數降序排序（reverse=True表示反向）
by_score = sorted(students, key=lambda s: s['score'], reverse=True)
print("按分數降序：", by_score)

# 按年級再按分數排序（使用元組作為key）
# Python會先按第一個元素(grade)排序，相同grade再按第二個元素(score)排序
by_grade_score = sorted(students, key=lambda s: (s['grade'], -s['score']))
print("按年級排序，同年級按分數降序：", by_grade_score)
