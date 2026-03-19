# R16. 過濾：推導式 / generator / filter / compress（1.16）

"""
本檔案示範四種常見過濾技巧：
1. 串列推導式（list comprehension）
2. 生成器表示式（generator expression）
3. filter(函式, 可迭代物件)
4. itertools.compress(資料, 布林遮罩)
"""

# ---------- 1) 串列推導式 / 2) 生成器表示式 ----------

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# 串列推導式：立即建立「新串列」，適合資料量不大或要重複使用結果。
positives = [n for n in mylist if n > 0]
negatives = [n for n in mylist if n < 0]

print("=== 串列推導式 ===")
print("原始資料：", mylist)
print("正數：", positives)
print("負數：", negatives)

# 生成器表示式：不會一次把結果全放到記憶體，會在迭代時才逐筆產生。
# 適合大量資料或只想逐筆消耗結果的情境。
pos_generator = (n for n in mylist if n > 0)

print("\n=== 生成器表示式 ===")
print("生成器物件本身：", pos_generator)
print("把生成器轉成 list：", list(pos_generator))
# 注意：生成器被消耗後就空了，再轉一次會得到空清單。
print("再次轉成 list（已被消耗）：", list(pos_generator))


# ---------- 3) filter ----------

values = ["1", "2", "-3", "-", "N/A", "5"]


def is_int(val: str) -> bool:
    """判斷字串是否可被安全轉成整數。"""
    try:
        int(val)
        return True
    except ValueError:
        return False


# filter 會把「判斷函式回傳 True」的元素留下來。
ivals = list(filter(is_int, values))

print("\n=== filter ===")
print("原始字串：", values)
print("可轉為整數者：", ivals)


# ---------- 4) itertools.compress ----------

from itertools import compress

addresses = ["A 區", "B 區", "C 區", "D 區"]
counts = [0, 3, 10, 7]

# 先建立布林遮罩（True 代表保留該位置元素）。
# 例如這裡是「只保留數量 > 5 的地址」。
more_than_five = [n > 5 for n in counts]
selected_addresses = list(compress(addresses, more_than_five))

print("\n=== compress ===")
print("地址：", addresses)
print("數量：", counts)
print("布林遮罩：", more_than_five)
print("數量 > 5 的地址：", selected_addresses)
