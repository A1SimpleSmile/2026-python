# R9. 兩字典相同點：keys/items 集合運算（1.9）

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# keys 的交集：同時出現在 a、b 的 key。
a.keys() & b.keys()

# keys 的差集：在 a 裡有，但 b 沒有的 key。
a.keys() - b.keys()

# items 的交集：key 和 value 都相同才算同一個 item。
a.items() & b.items()

# 字典推導：從 a 過濾掉不想要的 key（z、w）。
# 這裡等於建立「清理後」的新字典 c。
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
