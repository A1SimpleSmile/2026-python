# 10 模組、類別、例外與 Big-O（最低門檻）範例

# 匯入模組：從 collections 模組匯入 deque 類別
# deque 是雙端隊列，支援高效的兩端操作
from collections import deque

# 創建一個最大長度為 2 的 deque
# 當超過最大長度時，會自動移除最舊的元素
q = deque(maxlen=2)
q.append(1)  # 添加元素 1
q.append(2)  # 添加元素 2
q.append(3)  # 添加元素 3，自動移除最舊的 1

# 顯示 deque 的狀態
print("=== deque 示例 ===")
print("deque 內容:", list(q))  # 轉成列表查看
print()

# 類別定義
class User:
    # __init__ 是建構函式，在創建物件時自動呼叫
    def __init__(self, user_id):
        # self 代表物件本身
        # 設定物件的屬性
        self.user_id = user_id

# 創建 User 物件
u = User(42)
# 存取物件的屬性
uid = u.user_id

print("=== 類別示例 ===")
print(f"用戶 ID: {uid}")
print()

# 例外處理
def is_int(val):
    # try-except 區塊用於處理可能發生的例外
    try:
        # 嘗試將 val 轉換為整數
        int(val)
        # 如果成功，返回 True
        return True
    except ValueError:
        # 如果發生 ValueError（轉換失敗），返回 False
        return False

# 測試例外處理函式
print("=== 例外處理示例 ===")
test_values = ["123", "abc", "45.6", "0"]
for val in test_values:
    result = is_int(val)
    print(f"is_int('{val}') = {result}")
print()

# Big-O 只是觀念提示
# Big-O 表示演算法的時間或空間複雜度
# list.append 通常是 O(1) - 常數時間
# list 切片是 O(N) - 線性時間，N 是列表長度

print("=== Big-O 概念示例 ===")
# O(1) 操作示例
my_list = []
for i in range(5):
    my_list.append(i)  # O(1) 操作
print("O(1) 操作 - append:", my_list)

# O(N) 操作示例
sliced = my_list[1:4]  # O(N) 操作
print("O(N) 操作 - 切片:", sliced)
print()

print("=== 更多模組使用示例 ===")
# 使用 collections 的其他功能
from collections import Counter

# Counter 用於計數
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print("單字計數:", dict(word_count))

# 使用 defaultdict
from collections import defaultdict
dd = defaultdict(int)
for word in words:
    dd[word] += 1
print("defaultdict 計數:", dict(dd))
print()

print("=== 類別進階示例 ===")
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        # 方法：類別內的函式
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        else:
            return 'F'

# 創建學生物件
students = [
    Student("Alice", 95),
    Student("Bob", 87),
    Student("Charlie", 72)
]

print("學生成績:")
for student in students:
    print(f"{student.name}: {student.score} 分 - 等級 {student.get_grade()}")
print()

print("=== 例外處理進階示例 ===")
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "錯誤：除數不能為零"
    except TypeError:
        return "錯誤：輸入必須是數字"
    finally:
        # finally 區塊總是會執行
        print("safe_divide 函式執行完畢")

# 測試例外處理
test_cases = [(10, 2), (10, 0), (10, "a")]
for a, b in test_cases:
    result = safe_divide(a, b)
    print(f"safe_divide({a}, {b}) = {result}")
print()

print("=== Big-O 實務應用 ===")
import time

# 比較不同操作的效能
def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start

# 創建大列表
large_list = list(range(10000))

# O(1) 操作
_, time_append = measure_time(lambda: large_list.append(10000))
print(".4f")

# O(N) 操作
_, time_slice = measure_time(lambda: large_list[5000:6000])
print(".4f")

# O(N) 搜尋
_, time_search = measure_time(lambda: 9999 in large_list)
print(".4f")
