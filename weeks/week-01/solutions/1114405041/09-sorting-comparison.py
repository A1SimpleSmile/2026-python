# 9 比較、排序與 key 函式範例

# 比較運算（tuple 逐一比較）
# 元組比較是從左到右逐元素比較，直到找到第一個不同的元素
a = (1, 2)
b = (1, 3)
result = a < b  # 比較結果：True，因為 a[1] < b[1]

# key 排序
# sorted() 函式使用 key 參數來自定義排序規則
# lambda r: r['uid'] 表示以每個字典的 'uid' 鍵值作為排序依據
rows = [{'uid': 3}, {'uid': 1}, {'uid': 2}]
rows_sorted = sorted(rows, key=lambda r: r['uid'])  # 按 uid 升序排序

# min/max 搭配 key
# min() 和 max() 也可以使用 key 參數來自定義比較規則
smallest = min(rows, key=lambda r: r['uid'])  # 找到 uid 最小的字典

# 顯示結果
print("=== 基本比較示例 ===")
print(f"a = {a}, b = {b}")
print(f"a < b: {result}")
print()

print("=== 排序示例 ===")
print("原始數據:", rows)
print("按 uid 排序後:", rows_sorted)
print()

print("=== min/max 示例 ===")
print("uid 最小的項目:", smallest)
largest = max(rows, key=lambda r: r['uid'])
print("uid 最大的項目:", largest)
print()

print("=== 更多比較示例 ===")
# 字串比較
str1 = "apple"
str2 = "banana"
print(f"'{str1}' < '{str2}': {str1 < str2}")  # 按字典順序比較

# 列表比較
list1 = [1, 2, 3]
list2 = [1, 2, 4]
print(f"{list1} < {list2}: {list1 < list2}")  # 逐元素比較
print()

print("=== 高級排序示例 ===")
# 複雜的排序：按多個鍵排序
students = [
    {'name': 'Alice', 'age': 25, 'score': 85},
    {'name': 'Bob', 'age': 20, 'score': 92},
    {'name': 'Charlie', 'age': 25, 'score': 78}
]

# 先按年齡升序，再按分數降序
sorted_students = sorted(students, key=lambda s: (s['age'], -s['score']))
print("學生數據:", students)
print("按年齡升序，分數降序排序:")
for student in sorted_students:
    print(f"  {student}")
print()

print("=== 優先級排序示例 ===")
# 模擬任務優先級排序 (priority, index, item)
tasks = [
    (2, 1, '低優先級任務'),
    (1, 3, '高優先級任務'),
    (1, 1, '最高優先級任務'),
    (3, 2, '最低優先級任務')
]

sorted_tasks = sorted(tasks)
print("任務列表 (優先級, 索引, 描述):")
for task in tasks:
    print(f"  {task}")
print("排序後 (優先級高的在前):")
for task in sorted_tasks:
    print(f"  {task}")
print()

print("=== 使用 operator.itemgetter ===")
from operator import itemgetter

# itemgetter 可以替代 lambda 函式，更高效
data = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]

sorted_by_score = sorted(data, key=itemgetter('score'))
print("使用 itemgetter 按分數排序:")
for item in sorted_by_score:
    print(f"  {item}")

# 多鍵排序
sorted_by_name_score = sorted(data, key=itemgetter('name', 'score'))
print("按姓名和分數排序:")
for item in sorted_by_name_score:
    print(f"  {item}")
