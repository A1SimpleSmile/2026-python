# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# re.compile / findall / sub / IGNORECASE / 非貪婪 / DOTALL

"""
本檔案涵蓋五個正則表達式核心技巧：
  2.4 re.compile / findall / finditer / match ── 搜尋與擷取
  2.5 re.sub / re.subn / 命名群組            ── 搜尋與替換
  2.6 re.IGNORECASE                           ── 忽略大小寫
  2.7 非貪婪 .*?                              ── 最短匹配
  2.8 re.DOTALL                               ── 讓 . 也能匹配換行
"""

import re

# ══ 2.4 匹配和搜尋 ════════════════════════════════════════════════════

text = "Today is 11/27/2012. PyCon starts 3/13/2013."
print("=== 2.4 搜尋與擷取 ===")
print("原始字串：", text)

# re.compile 預先編譯正則，適合在迴圈內重複使用，效能較好。
# (\d+) 是「捕獲分組」，會把括號內匹配到的文字單獨存起來方便取用。
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
# 格式：(月)/(日)/(年)

# findall：找出所有匹配，有捕獲分組時回傳 tuple 的 list。
all_dates = datepat.findall(text)
print("findall 結果：", all_dates)
# [('11', '27', '2012'), ('3', '13', '2013')]

# match：只從「字串開頭」比對，回傳 Match 物件或 None。
# group(0) 整個匹配字串；group(1/2/3) 各捕獲分組；groups() 所有分組的 tuple。
m = datepat.match("11/27/2012")
assert m is not None, "應該要匹配成功"
print(f"match group(0)={m.group(0)}, groups={m.groups()}")

# search：在字串任意位置找第一個匹配（match 只找開頭）。
m2 = datepat.search(text)
print(f"search 第一個匹配：{m2.group(0) if m2 else None}")

# finditer：回傳迭代器，每次產出一個 Match 物件，記憶體比 findall 省。
print("finditer 逐一取出並重新格式化：")
for m in datepat.finditer(text):
    month, day, year = m.groups()   # 用解包直接取三個分組
    print(f"  {year}-{month:>02}-{day:>02}")   # 改成 ISO 8601 格式


# ══ 2.5 搜尋和替換 ════════════════════════════════════════════════════

print("\n=== 2.5 sub 搜尋替換 ===")

# re.sub(pattern, repl, string)
# repl 字串中用 \1 \2 \3 反向引用第 1/2/3 個捕獲分組。
result1 = re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print("數字反向引用替換：", result1)
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# 命名群組 (?P<name>...) 讓模式更可讀；
# 替換字串用 \g<name> 引用。
result2 = re.sub(
    r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
    r"\g<year>-\g<month>-\g<day>",
    text,
)
print("命名群組替換：  ", result2)

# subn 同 sub，但額外回傳「實際替換次數」，方便確認有沒有真的改到。
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"subn 替換次數：{n}，結果：{newtext}")

# repl 也可以是「函式」，接收 Match 物件並回傳替換字串，
# 適合需要動態計算替換值的場合。
def date_fmt(m: re.Match) -> str:
    """把月份補零後重新格式化。"""
    month, day, year = m.groups()
    return f"{year}-{int(month):02d}-{int(day):02d}"

result3 = re.sub(r"(\d+)/(\d+)/(\d+)", date_fmt, text)
print("repl 函式（補零）：", result3)


# ══ 2.6 忽略大小寫 ════════════════════════════════════════════════════

print("\n=== 2.6 IGNORECASE ===")
s = "UPPER PYTHON, lower python, Mixed Python"

# flags=re.IGNORECASE（縮寫 re.I）讓模式不分大小寫。
matches = re.findall("python", s, flags=re.IGNORECASE)
print("不分大小寫搜尋：", matches)
# ['PYTHON', 'python', 'Python']

# 替換時同樣套用 IGNORECASE：把所有 python 不論大小寫都換成 'snake'。
result4 = re.sub("python", "snake", s, flags=re.IGNORECASE)
print("不分大小寫替換：", result4)
# 注意：替換後統一變小寫 'snake'，原始大小寫不會保留。


# ══ 2.7 非貪婪（最短匹配）════════════════════════════════════════════

print("\n=== 2.7 非貪婪 .*? ===")
text2 = 'Computer says "no." Phone says "yes."'

# .* 是「貪婪」：會盡量往右延伸，吃到最後一個 " 才停止。
greedy = re.compile(r'"(.*)"').findall(text2)
print("貪婪  .*  ：", greedy)    # ['no." Phone says "yes.']  ← 跨越了兩個引號！

# .*? 是「非貪婪」：找到第一個可以結束的位置就停止。
lazy = re.compile(r'"(.*?)"').findall(text2)
print("非貪婪 .*?：", lazy)      # ['no.', 'yes.']  ← 分別匹配兩個引號內容

# 規則：有明確結束符號（如 "）時，優先用非貪婪避免過度匹配。


# ══ 2.8 多行匹配（DOTALL）════════════════════════════════════════════

print("\n=== 2.8 DOTALL 跨行匹配 ===")
code = "/* this is a\nmultiline comment */"

# 預設 . 不匹配換行字元 \n。
no_dotall = re.compile(r"/\*(.*?)\*/").findall(code)
print("不加 DOTALL：", no_dotall)   # []，因為 .* 無法跨過 \n

# re.DOTALL 讓 . 也能匹配 \n，使模式可以跨行。
with_dotall = re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code)
print("加上 DOTALL：", with_dotall)  # [' this is a\nmultiline comment ']

# 多段 C 風格註解的實際情境
code2 = "int x; /* 變數 x */ int y; /* 變數 y\n   說明 */"
comments = re.findall(r"/\*(.*?)\*/", code2, re.DOTALL)
print("擷取多段註解：", [c.strip() for c in comments])
