# R4. heapq 取 Top-N（1.4）

# `heapq` 是 Python 內建的「最小堆」工具。
# 最小堆特性：最小值會在索引 0 的位置。
import heapq

# 一組數字資料，後面示範如何取最大/最小前 N 筆。
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 取最大的 3 個值（不會改變原本 nums）。
heapq.nlargest(3, nums)

# 取最小的 3 個值（同樣不改原資料）。
heapq.nsmallest(3, nums)

# `heapq` 也可配合 key 用在複雜資料（如 dict）上。
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]

# 依據 price 欄位取最便宜的 1 筆。
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

# 若要做「持續地」取最小值，可以先把資料建成堆。
heap = list(nums)

# `heapify` 會原地轉成堆結構，時間複雜度 O(n)。
heapq.heapify(heap)

# 每次 `heappop` 都會彈出目前最小值，複雜度 O(log n)。
heapq.heappop(heap)
