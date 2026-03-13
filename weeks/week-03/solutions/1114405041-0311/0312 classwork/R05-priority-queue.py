# R5. 優先佇列 PriorityQueue（1.5）

# 用 `heapq` 自行包一個簡單的優先佇列。
import heapq

class PriorityQueue:
    def __init__(self):
        # `_queue` 存放堆資料。
        self._queue = []
        # `_index` 作為同優先權時的先後順序（穩定排序）。
        self._index = 0

    def push(self, item, priority):
        # 為了讓「數字越大優先權越高」，這裡存 -priority。
        # tuple 比較順序：先比 -priority，再比 _index。
        # 所以同優先權時會先出現較早 push 的元素（FIFO）。
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heappop 回傳最小 tuple，取最後一格就是原始 item。
        return heapq.heappop(self._queue)[-1]
