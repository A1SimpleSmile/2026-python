# R01. 字串分割與匹配（2.1–2.3）
# re.split() 多分隔符 / startswith / endswith / fnmatch

"""
本檔案涵蓋三個常見字串處理技巧：
  2.1 re.split() ── 以多種分隔符同時分割字串
  2.2 startswith / endswith ── 快速檢查字串開頭或結尾
  2.3 fnmatch / fnmatchcase ── 使用 Shell 通配符（glob）做模式比對
"""

import re
from fnmatch import fnmatch, fnmatchcase

# ══ 2.1 多界定符分割 ══════════════════════════════════════════════════

line = "asdf fjdk; afed, fjek,asdf, foo"
print("=== 2.1 re.split() 多分隔符 ===")
print("原始字串：", line)

# 字元集 [;,\s] 表示「分號、逗號或任何空白字元」皆可作為分隔符；
# \s* 表示分隔符後面可有零個或多個空白，一併吃掉。
result1 = re.split(r"[;,\s]\s*", line)
print("字元集分割：", result1)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# (?:...) 是「非捕獲分組」：建立分組以使用 | 交替比對，
# 但不會把分隔符本身保留在結果串列中（若改用普通捕獲分組 (,|;|\s)，分隔符會出現在結果裡）。
result2 = re.split(r"(?:,|;|\s)\s*", line)
print("非捕獲分組分割：", result2)

# 對比：若使用「捕獲分組」，分隔符會夾在結果中
result3 = re.split(r"(,|;|\s)\s*", line)
print("捕獲分組分割（分隔符會留下）：", result3)


# ══ 2.2 開頭 / 結尾匹配 ══════════════════════════════════════════════

print("\n=== 2.2 startswith / endswith ===")

filename = "spam.txt"
url = "http://www.python.org"

# endswith / startswith 接受「字串」或「字串的 tuple」；
# 注意：不能傳 list，必須是 tuple。
print(f'"{filename}".endswith(".txt")     =', filename.endswith(".txt"))    # True
print(f'"{filename}".startswith("file:") =', filename.startswith("file:"))  # False
print(f'"{url}".startswith(("http:", "https:")) =',
      url.startswith(("http:", "https:")))  # True

# 批次篩選：找出所有 .c 或 .h 結尾的檔案
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
c_or_h = [name for name in filenames if name.endswith((".c", ".h"))]
print("所有 .c / .h 檔案：", c_or_h)
# ['foo.c', 'spam.c', 'spam.h']

# 搭配 any()：只要有任何一個符合就為 True
print("有 .py 檔嗎？", any(name.endswith(".py") for name in filenames))  # True


# ══ 2.3 Shell 通配符匹配 ══════════════════════════════════════════════

print("\n=== 2.3 fnmatch / fnmatchcase ===")

# fnmatch 支援的萬用字元：
#   *   ── 任意長度的任意字元
#   ?   ── 恰好一個任意字元
#   [n] ── 字元集合，例如 [0-9] 表示數字
# fnmatch 的大小寫敏感性「依作業系統」決定（Windows 不分、Linux 分），
# fnmatchcase 則「強制區分」大小寫，跨平台行為一致。

print(fnmatch("foo.txt", "*.txt"))          # True，* 匹配任意字元
print(fnmatch("Dat45.csv", "Dat[0-9]*"))    # True，[0-9] 匹配單一數字
print(fnmatch("foo.txt", "foo?.txt"))        # False，? 只匹配一個字元

# fnmatchcase 強制區分大小寫（無論在哪個 OS 都一樣）
print(fnmatchcase("foo.txt", "*.TXT"))       # False，大小寫不同
print(fnmatchcase("FOO.TXT", "*.TXT"))       # True

# 實際應用：篩選符合特定街道模式的地址
addresses = [
    "5412 N CLARK ST",
    "1060 W ADDISON ST",
    "1039 W GRANVILLE AVE",
    "2122 N CLARK ST",
]
# 只保留結尾是 " ST" 的地址
st_addresses = [a for a in addresses if fnmatchcase(a, "* ST")]
print("結尾為 ST 的地址：", st_addresses)
# ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']

# fnmatch vs re：fnmatch 語法更簡單，適合類 glob 模式；
# 若需要更複雜的模式（如前後斷言、分組），才改用 re。
