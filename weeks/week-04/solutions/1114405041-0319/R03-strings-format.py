# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# strip / ljust / join / format / format_map / textwrap

"""
本檔案涵蓋五個字串處理技巧：
  2.11 strip / lstrip / rstrip  ── 清除首尾不需要的字元
  2.13 ljust / rjust / center   ── 對齊與填充
  2.14 join                     ── 高效拼接字串
  2.15 format / format_map / f-string ── 字串插值
  2.16 textwrap                 ── 指定列寬自動換行
"""

import textwrap

# ══ 2.11 清理字元 ════════════════════════════════════════════════════

print("=== 2.11 strip 清理首尾字元 ===")
s = "  hello world \n"
print(repr(s.strip()))          # 'hello world'  ← 兩端空白與換行全部移除
print(repr(s.lstrip()))         # 'hello world \n'  ← 只清左端
print(repr(s.rstrip()))         # '  hello world'   ← 只清右端

# strip 可以傳入「要移除的字元集合」（不是子字串，是字元集）
print("-----hello=====".strip("-="))   # 'hello'，把兩端的 - 與 = 全部剝除

# 實際應用：從檔案或 API 讀進來的字串通常有多餘空白，
# 存入資料庫或比對前先 strip() 是好習慣。
lines = ["  Alice  ", "Bob\t", "\nCarol"]
cleaned = [line.strip() for line in lines]
print("批次清理：", cleaned)   # ['Alice', 'Bob', 'Carol']


# ══ 2.13 字串對齊 ════════════════════════════════════════════════════

print("\n=== 2.13 對齊與填充 ===")
text = "Hello World"

# ljust / rjust / center 的第二個參數是填充字元（預設為空格）。
print(repr(text.ljust(20)))          # 'Hello World         '（靠左，右補空格）
print(repr(text.rjust(20)))          # '         Hello World'（靠右，左補空格）
print(repr(text.center(20, "*")))    # '****Hello World*****'（置中，用 * 填充）

# format() 格式規格：[填充字元][對齊方向][總寬度][.精度][型別]
# < 靠左  > 靠右  ^ 置中
print(format(text, "<20"))           # 靠左（與 ljust 等效）
print(format(text, ">20"))           # 靠右
print(format(text, "^20"))           # 置中
print(format(text, "*^20"))          # 置中並用 * 填充

# 數字格式化：> 靠右、.2f 保留兩位小數
print(format(1.2345, ">10.2f"))      # '      1.23'
print(format(1234567, ","))          # '1,234,567'（千分位）
print(format(0.1234, ".1%"))         # '12.3%'（百分比）

# 製作對齊表格報表
headers = ["股票", "數量", "單價"]
rows = [("ACME", 100, 45.23), ("AAPL", 50, 612.78), ("IBM", 75, 205.55)]
print(f"\n{'股票':<8} {'數量':>6} {'單價':>10}")
print("-" * 28)
for name, shares, price in rows:
    print(f"{name:<8} {shares:>6} {price:>10.2f}")


# ══ 2.14 合併拼接 ════════════════════════════════════════════════════

print("\n=== 2.14 join 拼接 ===")
parts = ["Is", "Chicago", "Not", "Chicago?"]

# 用 join 而不是 + 做迴圈拼接，效能差異在資料量大時非常顯著。
# + 每次拼接都建立新字串物件；join 只建立一次。
print(" ".join(parts))    # 'Is Chicago Not Chicago?'
print(",".join(parts))    # 'Is,Chicago,Not,Chicago?'
print("".join(parts))     # 'IsChicagoNotChicago?'（無分隔符）

# join 要求每個元素都是字串，非字串需先轉換。
data = ["ACME", 50, 91.1]
print(",".join(str(d) for d in data))   # 'ACME,50,91.1'
# 生成器表達式在這裡比先建 list 再 join 稍微省記憶體。


# ══ 2.15 插入變量 ════════════════════════════════════════════════════

print("\n=== 2.15 字串插值 ===")
name, n = "Guido", 37
template = "{name} has {n} messages."

# 方式一：str.format()，明確傳入關鍵字引數。
print(template.format(name=name, n=n))

# 方式二：format_map(vars())，把當前區域變數字典傳入，
# 不用一一列出變數名稱，但使用者需確保模板中的變數名都已定義。
print(template.format_map(vars()))

# 方式三：f-string（Python 3.6+），最簡潔且效能最佳，
# 直接在 {} 內寫運算式。
print(f"{name} has {n} messages.")
print(f"平方：{n ** 2}")          # {} 內可放任意運算式
print(f"大寫：{name.upper()}")    # 也可呼叫方法


# ══ 2.16 指定列寬（textwrap）════════════════════════════════════════

print("\n=== 2.16 textwrap 自動換行 ===")
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)

# fill：把長字串折成指定寬度的段落字串。
print("--- 寬度 40 ---")
print(textwrap.fill(long_s, 40))

# initial_indent：第一行縮排；subsequent_indent：後續行縮排。
print("\n--- 首行縮排 4 格 ---")
print(textwrap.fill(long_s, 40, initial_indent="    "))

print("\n--- 每行縮排 4 格（模擬引用段落）---")
print(textwrap.fill(long_s, 40, initial_indent="    ", subsequent_indent="    "))

# shorten：截短並加上省略號，適合顯示摘要。
print("\n--- shorten 截短摘要 ---")
print(textwrap.shorten(long_s, width=50, placeholder=" ..."))
