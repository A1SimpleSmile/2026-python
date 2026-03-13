# R8. 字典運算：min/max/sorted + zip（1.8）

# prices: 股票代號 -> 價格
prices = {'ACME': 45.23, 'AAPL': 612.78, 'FB': 10.75}

# zip(values, keys) 會產生 (price, symbol) tuple，
# tuple 比較先看第一欄，所以可直接拿到最小/最大價格與對應代號。
min(zip(prices.values(), prices.keys()))
max(zip(prices.values(), prices.keys()))

# sorted 可列出由小到大排序後的全部 (price, symbol)。
sorted(zip(prices.values(), prices.keys()))

# 另一種方式：直接在 key 上找最小價格的代號。
# 注意這行回傳的是 key（例如 'FB'），不是價格本身。
min(prices, key=lambda k: prices[k])  # 回傳 key
