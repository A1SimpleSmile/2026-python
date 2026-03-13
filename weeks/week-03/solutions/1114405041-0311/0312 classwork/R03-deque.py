# R3. deque 保留最後 N 筆（1.3）

# `deque`（double-ended queue，雙端佇列）可在左右兩端高效率插入/刪除。
# 常見用途：
# 1. 保留最近 N 筆資料（滑動視窗）
# 2. 需要從頭尾都快速取放元素的情境
from collections import deque

# 設定 maxlen=3：表示最多只保留 3 個元素。
# 超過容量時，會「自動移除最舊元素」（左邊那個）。
q = deque(maxlen=3)

# 依序加入 1、2、3。
q.append(1); q.append(2); q.append(3)

# 再加入 4 時，容量已滿，最舊的 1 會被自動丟掉。
# 最終 q 會是 deque([2, 3, 4], maxlen=3)
q.append(4)  # 自動丟掉最舊的 1

# 不設定 maxlen 時，deque 長度可持續成長。
q = deque()

# append(x): 從右邊加入
# appendleft(x): 從左邊加入
# 執行後 q 內容會是 [2, 1]
q.append(1); q.appendleft(2)

# pop(): 從右邊移除並回傳
# popleft(): 從左邊移除並回傳
# 這兩個操作常用在「先進先出」或「兩端操作」的資料處理。
q.pop(); q.popleft()
