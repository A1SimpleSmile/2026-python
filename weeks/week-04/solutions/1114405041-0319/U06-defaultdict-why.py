# U6. defaultdict 為何比手動初始化乾淨（1.6）

"""
重點說明：
  一般 dict 在存取不存在的 key 時會拋出 KeyError；
  若要「累積」資料（同一個 key 對應多個值），必須先判斷 key 是否存在再初始化。
  defaultdict(factory) 會在存取不存在的 key 時，自動呼叫 factory() 建立預設值，
  省去所有「if key not in d」的初始化分支，讓程式碼更簡潔。

  factory 可以是任何零引數可呼叫物件：
    - list    → 預設值為 []
    - int     → 預設值為 0
    - set     → 預設值為 set()
    - lambda: 'N/A' → 預設值為字串 'N/A'
"""

from collections import defaultdict

pairs = [("a", 1), ("a", 2), ("b", 3), ("c", 10), ("b", 5)]

# ── 示範一：手動版（必須一直判斷 key 是否存在）────────────────────────
d_manual = {}
for k, v in pairs:
    if k not in d_manual:   # 若 key 不存在就先建立空 list
        d_manual[k] = []
    d_manual[k].append(v)   # 再把值加進去

print("=== 手動版（if k not in d）===")
print(d_manual)   # {'a': [1, 2], 'b': [3, 5], 'c': [10]}

# ── 等效寫法：用 dict.setdefault() ────────────────────────────────────
# setdefault(key, default) 如果 key 不存在就設入 default 再回傳，
# 比手動 if 稍短，但每次都要帶預設值參數，可讀性不如 defaultdict。
d_setdefault = {}
for k, v in pairs:
    d_setdefault.setdefault(k, []).append(v)

print("\n=== setdefault 版 ===")
print(d_setdefault)

# ── 示範二：defaultdict(list) 版（最乾淨）───────────────────────────
# 存取不存在的 key 時自動呼叫 list()，建立空 list 作為預設值，
# 不需要任何 if 判斷，直接 .append() 即可。
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)   # key 不存在時自動初始化為 []

print("\n=== defaultdict(list) 版 ===")
print(dict(d2))   # 轉成普通 dict 以便顯示

# ── 示範三：defaultdict(int) 做計數器 ────────────────────────────────
# int() 回傳 0，因此 key 不存在時預設值為 0，可直接做 += 。
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = defaultdict(int)
for word in words:
    counter[word] += 1   # key 不存在時自動設為 0，再加 1

print("\n=== defaultdict(int) 計數器 ===")
for word, count in sorted(counter.items()):
    print(f"  {word}: {count}")

# ── 示範四：defaultdict(set) 做一對多去重 ────────────────────────────
# set() 回傳空集合，適合「同一個 key 對應多個不重複值」的場景。
relations = [
    ("Alice", "Bob"), ("Alice", "Carol"),
    ("Bob",   "Alice"), ("Alice", "Bob"),   # 重複的會被 set 過濾掉
]
graph = defaultdict(set)
for src, dst in relations:
    graph[src].add(dst)

print("\n=== defaultdict(set) 關係圖 ===")
for person, friends in sorted(graph.items()):
    print(f"  {person} → {sorted(friends)}")

# ── 示範五：存取不存在的 key 時 defaultdict 的副作用 ─────────────────
# 注意：只要「讀取」不存在的 key，defaultdict 就會自動建立該 key。
# 若只想查詢是否存在，應改用 .get() 或先用 in 判斷，避免汙染字典。
d3 = defaultdict(list)
d3["x"].append(1)
_ = d3["y"]   # 純讀取不存在的 key → 自動建立 y: []

print("\n=== 讀取不存在的 key 會自動建立 ===")
print(dict(d3))   # {'x': [1], 'y': []}  ← y 被自動建立了！
print("建議改用 .get()：", d3.get("z"))   # None，不會建立 z

