# AI_USAGE.md - AI 協助使用記錄

本文件記錄 Week 02（Task 1/2/3）中 AI 協助使用方式與反思。


### 問題 5：如何判斷測試案例設計是否充分？

**我的提問：**
> 我該設計多少測試案例？「正常、邊界、反例」之外還有什麼？

**AI 的建議：**
- 最少 3 種：正常（包含預期的中等複雜度）、邊界（最小/最大/空）、反例（容易誤寫的情況）
- 加分項：同時測試多個規則交互的案例（如「同分同年齡按名稱」）
- 驗證方法：用等價類劃分（Equivalence Partitioning）思考

**我的選擇：** 採納建議，並額外設計「多條件交互」測試
- 理由：對應作業複雜度，Task 2 與 Task 3 本質上都是多層條件
- 驗證：每個 TEST_CASES.md 中的案例都對應至少一個測試函式

---

## 2. 採納的 AI 建議（與效果）

### 建議 1：使用 `defaultdict` 配合 `Counter`

**AI 的建議：**
> Task 3 中，若要同時統計使用者和操作，可使用 `defaultdict(int)` 配合 `Counter`

**我的實作：**
```python
from collections import Counter, defaultdict

user_counter = Counter()
action_counter = Counter()

for user, action in logs:
    user_counter[user] += 1
    action_counter[action] += 1
```

**效果：** ✅ 程式碼簡潔、易讀，自動處理缺失鍵

---

### 建議 2：在測試中使用 `setUp()` 方法準備共享資料

**AI 的建議：**
> 多個測試方法使用相同的測試資料時，在 `setUp()` 中初始化，避免重複

**我的實作：**
```python
class TestRankStudents(unittest.TestCase):
    def setUp(self):
        """準備測試資料"""
        self.students = [
            ("amy", 88, 20),
            ("bob", 88, 19),
            # ...
        ]
    
    def test_rank_normal(self):
        result = rank_students(self.students, 3)
        # ...
```

**效果：** ✅ 程式碼更乾淨，資料修改時只需改一處

---

### 建議 3：將解析邏輯分離成獨立函式

**AI 的建議：**
> 不要在 `main()` 中做解析，應提取 `parse_student()` 等函式，便於測試

**我的實作：**
```python
def parse_student(line):
    """解析學生資料行"""
    parts = line.split()
    name = parts[0]
    score = int(parts[1])
    age = int(parts[2])
    return (name, score, age)

def main():
    n, k = map(int, input().split())
    students = []
    for _ in range(n):
        line = input().strip()
        name, score, age = parse_student(line)
        students.append((name, score, age))
    # ...
```

**效果：** ✅ 測試時可獨立測試 parse，不需 mock input

---

### 建議 4：使用 `maxResults` 限制測試輸出

**AI 的建議：**
> 執行測試時加 `-v` 參數，能清楚看到每個測試的通過/失敗

**我的實作：**
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

**效果：** ✅ 調試時能快速判斷是哪個測試失敗

---

## 3. 拒絕的 AI 建議（與原因）

### 建議 1（拒絕）：使用 `pandas` 進行去重

**AI 的建議：**
> 使用 pandas 的 `drop_duplicates()` 能一行搞定去重

**我的拒絕理由：**
- 作業要求「練習 Python 序列處理」，引入 pandas 違背初衷
- 題目明言「不可用 set 直接輸出去重結果」，隱含要自己實作邏輯
- pandas 不在作業推薦套件中

---

### 建議 2（拒絕）：使用遞迴實作排序

**AI 的建議：**
> 可以用快速排序遞迴實作，加深對排序演算法的理解

**我的拒絕理由：**
- 題目明言「必須使用 `sorted(..., key=...)`」，不允許自寫排序
- 遞迴排序容易出現堆棧溢出，不適合這類數據量適中的題目
- 目標是掌握 `sorted()` 的 `key` 參數，不是重造輪子

---

### 建議 3（拒絕）：使用 `unittest.TestLoader` 動態生成測試

**AI 的建議：**
> 可以用 `TestLoader` 與 `@parameterized` 裝飾器定義參數化測試

**我的拒絕理由：**
- 題目要求「測試骨架由學生自行撰寫」，參數化測試框架違背要求
- 會引入 `parameterized` 套件，額外依賴
- 手寫測試方法更易於理解和調試

---

### 建議 4（拒絕）：輸出格式用 f-string 的複雜格式

**AI 的建議：**
> 可以用 f-string 內的三元運算子判斷是否輸出 evens

**我的拒絕理由：**
- 過度複雜，降低可讀性
- 題目要求輸出「evens: ...」，無需條件判斷該行是否存在

---

## 4. AI 誤導案例與自行修正

### 案例 1：Counter 排列順序誤解

**AI 的初始說法：**
> 當 action 出現次數都不同時，`most_common()` 自動按次數排序。但多個 action 同次數時順序不確定，需自己排序

**我遇到的問題：**
實作後測試 `test_summarize_tie_break_by_name` 失敗，輸出順序亂糟糟

**我自行發現：**
```python
# 錯誤做法（只取最常見但未考慮平手）
top_action, top_action_count = action_counter.most_common(1)[0]

# 題目要求「全域最常見 action」，就是最多次數的單數個
# 無需考慮平手，most_common(1) 自動返回第一個最多的
```

**修正方式：**
```python
if action_counter:
    top_action, top_action_count = action_counter.most_common(1)[0]
else:
    top_action, top_action_count = None, 0
```

**學到：** 每個題目只要求「第一個」最常見，無需額外排序。題目用單數「action」這個細節很重要。

---

### 案例 2：排序穩定性誤用

**AI 的建議：**
> 先按名稱排序，再按分數排序，利用穩定排序的特性達到多層排序

**我遇到的問題：**
初次嘗試這方法時，分層排序順序搞反了

```python
# 錯誤（順序反了）
result = sorted(students, key=lambda x: (x[0]))  # 先按名稱
result = sorted(result, key=lambda x: (-x[1]))   # 再按分數
```

**自行修正：**
```python
# 正確（一次三層排序）
result = sorted(students, key=lambda x: (-x[1], x[2], x[0]))
```

**學到：** 一次性定義多層 key 比分次排序更安全、更快。分次排序需記住「從低優先級往高優先級排」。

---

### 案例 3：邊界條件遺漏

**AI 的說法：**
> 測試 Task 1 時考慮「空列表、單一元素、全部相同」就夠了

**我遇到的問題：**
測試通過後，執行時卻發現輸出格式在「偶數為空」時異常

```python
# 生成的初版 main()
evens_result = get_evens(numbers)
print(f"evens: {' '.join(map(str, evens_result))}")  # 空時輸出 "evens: "
```

**自行補測：**
設計 `test_evens_no_even` 測試案例，驗證空結果輸出格式

**修正：** 實際上無需修改程式（空列表 join 結果為空字串），但認識到邊界不止「空輸入」還有「空結果」。

**學到：** 邊界分為：輸入邊界（空、單一、極大）與 輸出邊界（空結果、單一結果、極大結果）

---

## 5. 總體反思

### 有效的 AI 協助方式
1. **Ask Why：** 提問「為什麼選這方案」而不是直接要程式碼
2. **設計先行：** 先討論設計（如排序鍵），再動手實作
3. **舉例驗證：** 讓 AI 舉具體例子驗證邏輯正確性

### AI 可能誤導的情況
1. **過度簡化：** 建議太簡單的方案，未考慮邊界
2. **套件選擇：** 傾向推薦流行套件，但作業有特定限制
3. **一知半解：** 某些細節（如 Counter 平手）說不清楚，需親自驗證

### 改進策略
1. **編寫測試先行：** 定義清楚的預期，再用測試驗證
2. **保持質疑：** AI 的建議不一定對，特別是細節上
3. **實驗驗證：** 關鍵邏輯自己寫測試驗證，不憑感覺

---

## 6. 建議後進者

基於本次經驗，給後來學生的建議：

1. **充分理解題意：** 「全域最常見」是單數，不用考慮平手
2. **設計測試案例：** 邊界不只「空輸入」還有「空結果」和「多條件交互」
3. **質疑 AI：** 特別是排序、統計這類易出錯的地方，一定親自驗證
4. **版本控制：** 每次通過測試就 commit，便於回溯誤改
5. **分離邏輯：** Parse、核心、輸出分離，便於測試和維護

