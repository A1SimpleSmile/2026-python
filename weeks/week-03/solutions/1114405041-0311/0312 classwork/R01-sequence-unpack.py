# R1. 序列解包（1.1）

# `p` 是一個 tuple（元組），裡面有兩個值 4、5。
p = (4, 5)

# 序列解包（unpacking）：左邊兩個變數會依序接住右邊 tuple 的第 1、2 個元素。
# 等價概念：x = p[0], y = p[1]
x, y = p

# `data` 是 list（串列），長度為 4。
# 第 4 個元素本身又是一個 tuple（日期：年、月、日）。
data = ['ACME', 50, 91.1, (2012, 12, 21)]

# 基本解包：左邊有 4 個變數，必須對應到右邊 4 個元素。
# 對應關係：
# name   <- 'ACME'
# shares <- 50
# price  <- 91.1
# date   <- (2012, 12, 21)
name, shares, price, date = data

# 巢狀解包：最後一格原本是 `date`（一個 tuple），
# 這裡直接再往內解成 year、mon、day。
# 這種寫法的好處是：後面就不用再寫 year, mon, day = date。
name, shares, price, (year, mon, day) = data

# 丟棄不需要的值（占位）
# `_` 常被當成「我不打算使用這個值」的慣例名稱。
# 注意：`_` 並不是真的忽略，只是你選擇不用它。
# 這行代表：只取 shares、price，其餘位置用 `_` 接住。
_, shares, price, _ = data
