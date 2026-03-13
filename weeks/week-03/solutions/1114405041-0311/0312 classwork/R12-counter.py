# R12. Counter 統計 + most_common（1.12）

# Counter 是字典子類，專門做次數統計。
from collections import Counter

# 一串單字資料。
words = ['look', 'into', 'my', 'eyes', 'look']

# 建立次數表，例如 {'look': 2, 'into': 1, ...}
word_counts = Counter(words)

# most_common(3): 取出前 3 名 (元素, 次數)
word_counts.most_common(3)

# update 可再追加統計，不會覆蓋原次數。
word_counts.update(['eyes', 'eyes'])
