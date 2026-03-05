# 10 模組、類別、例外與 Big-O（最低門檻）範例
# ===========================================
# 本文件演示四個重要概念：導入模組、定義類別、處理異常、認識演算法複雜度

# ============================================
# ◆ 範例1：模組與導入 (Import & Module)
# ============================================
# 模組(module)是包含Python程式碼的文件或包
# 導入(import)是將模組中的功能引入當前程式

# 從collections模組導入deque(雙端隊列)
# deque是一個優化的列表，適合從両端快速添加/移除元素
from collections import deque

# 創建一個最多保存2個元素的deque
# 當超過maxlen時，會自動刪除最舊的元素（FIFO隊列行為）
q = deque(maxlen=2)

q.append(1)  # 隊列: [1]
print(f"append(1)後: {list(q)}")

q.append(2)  # 隊列: [1, 2]
print(f"append(2)後: {list(q)}")

q.append(3)  # 隊列: [2, 3]  - 自動丟掉最舊的元素1
print(f"append(3)後: {list(q)}")

# ============================================
# ◆ 範例2：類別與物件 (Class & Object)
# ============================================
# 類別(class)是藍圖，用來建立具有相同屬性和方法的物件
# 物件(object)是類別的實例(instance)

class User:
    """
    用戶類別
    属性(attribute): user_id - 用戶的唯一識別符
    """
    
    # __init__ 是建構函式(constructor)
    # 當用User(...)建立物件時會自動調用
    # self參數代表即將被建立的物件本身
    def __init__(self, user_id):
        # 為這個物件設置user_id屬性
        self.user_id = user_id
        print(f"已建立用戶，ID: {user_id}")

# 使用User類別建立一個物件實例
# 這會觸發__init__()方法
u = User(42)

# 訪問物件的屬性
uid = u.user_id
print(f"訪問用戶ID: {uid}")

# 建立多個物件實例
user2 = User(100)
user3 = User(200)
print(f"user2的ID: {user2.user_id}")
print(f"user3的ID: {user3.user_id}")

# ============================================
# ◆ 範例3：例外處理 (Exception Handling)
# ============================================
# 例外(exception)是程式執行時發生的錯誤
# try-except 是捕捉和處理例外的方式

def is_int(val):
    """
    檢查一個值是否能轉換為整數
    參數: val - 任何Python物件
    返回: True如果能轉換，False如果不能
    """
    try:
        # 嘗試將val轉換為整數
        int(val)
        # 如果成功，返回True
        return True
    except ValueError:
        # 如果轉換失敗(拋出ValueError)，執行此塊
        # ValueError表示「値が合っていない」(値の形式が正しくない)
        return False
    except Exception as e:
        # 捕捉任何其他未預期的例外
        print(f"未預期的錯誤: {e}")
        return False

# 測試is_int()函式
print("\n--- 例外處理測試 ---")
print(f"is_int('123'): {is_int('123')}")  # True - '123'是數字字符串
print(f"is_int('abc'): {is_int('abc')}")  # False - 'abc'無法轉換為整數
print(f"is_int(42): {is_int(42)}")        # True - 42已經是整數
print(f"is_int(3.14): {is_int(3.14)}")    # True - 3.14能轉換為整數

# 更多例外處理場景
def safe_divide(a, b):
    """安全的除法函式，處理除以零的情況"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        # 特定處理除以零的錯誤
        print(f"錯誤：不能除以0")
        return None
    except TypeError:
        # 處理類型錯誤（例如字符串和數字相除）
        print(f"錯誤：操作數類型不匹配")
        return None
    except Exception as e:
        # 捕捉任何其他異常
        print(f"未預期的錯誤: {e}")
        return None

print(f"\nsafe_divide(10, 2): {safe_divide(10, 2)}")  # 5.0
print(f"safe_divide(10, 0): {safe_divide(10, 0)}")    # None (被捕捉)

# ============================================
# ◆ 範例4：Big-O 時間複雜度概念 (Big-O Notation)
# ============================================
# Big-O用來描述演算法在最壞情況下的性能
# 幫助我們理解演算法快或慢的相對關係

# 常見的Big-O符號及含義
# O(1) - 常數時間：無論輸入有多大，執行時間固定（最快）
# O(log N) - 對數時間：例如二分查找
# O(N) - 線性時間：執行時間與N成正比
# O(N log N) - 例如efficient排序
# O(N²) - 二次方：例如bubble sort
# O(2^N) - 指數時間：非常慢（最慢）

print("\n--- Big-O 時間複雜度示例 ---")

# 例子1: list.append() 通常是 O(1)
lst = [1, 2, 3]
lst.append(4)  # 不管列表有多長，append新元素耗時都相同
print("list.append(4)的時間複雜度: O(1) - 常數時間")

# 例子2: list切片是 O(N)
lst1 = [1, 2, 3, 4, 5]
lst2 = lst1[1:4]  # 需要遍歷並複製3個元素
# 如果列表有1000個元素，切片就要複製相應多的元素
print("list切片[1:4]的時間複雜度: O(N) - 線性時間")

# 例子3: 簡單迴圈 - O(N)
def print_all(items):
    """遍歷並打印所有項目 - O(N)"""
    for item in items:  # 循環次數與items長度成正比
        print(item)

# 例子4: 巢狀迴圈 - O(N²)
def bubble_sort_demo(arr):
    """氣泡排序示例 - O(N²)"""
    n = len(arr)
    for i in range(n):           # 外層迴圈: N次
        for j in range(n - 1):   # 內層迴圈: N次
            # 比較和交換
            pass
    # 總執行次數: N × N = N²

# Big-O快速參考表
print("\n--- Big-O量級比較 (輸入N=1000時) ---")
operations = {
    "O(1)": 1,
    "O(log N)": 10,
    "O(N)": 1000,
    "O(N log N)": 10000,
    "O(N²)": 1000000,
    "O(2^N)": "太大了！(超過10^300)"
}
for notation, ops in operations.items():
    print(f"{notation}: ~{ops} 次操作")

print("\n💡 結論：優先選擇時間複雜度低的演算法，避免O(N²)及以上！")
