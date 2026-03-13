# R11. 命名切片 slice（1.11）

# 模擬固定欄位格式字串（例如舊系統報表行）。
record = '....................100 .......513.25 ..........'

# 用 slice 命名欄位位置，讓程式可讀性更高。
SHARES = slice(20, 23)
PRICE = slice(31, 37)

# 透過命名切片取出欄位，再做型別轉換與計算。
cost = int(record[SHARES]) * float(record[PRICE])
