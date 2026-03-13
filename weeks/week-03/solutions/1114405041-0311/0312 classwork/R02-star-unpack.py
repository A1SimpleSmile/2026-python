# R2. 解包數量不固定：星號解包（1.2）

# 這個函式示範「頭尾固定，中間長度不固定」的解包模式。
def drop_first_last(grades):
    # `first` 取第一個成績，`last` 取最後一個成績，
    # `*middle` 會把中間全部元素收集成 list。
    # 例如 grades = [98, 76, 88, 91, 83]
    # first=98, middle=[76, 88, 91], last=83
    first, *middle, last = grades

    # 這裡只計算中間成績平均，忽略第一個與最後一個。
    # 常見用途：去掉極端值後再計算平均。
    return sum(middle) / len(middle)

# 這個 tuple 有 4 個欄位：姓名、email、電話1、電話2
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

# 前兩個欄位固定接收，剩下全部收進 `phone_numbers`（list）。
# 結果：
# name = 'Dave'
# email = 'dave@example.com'
# phone_numbers = ['773-555-1212', '847-555-1212']
name, email, *phone_numbers = record

# 星號也可以放在前面：
# `current` 拿最後一個值，前面的全部收進 `trailing`。
# 結果：current = 3, trailing = [10, 8, 7, 1, 9, 5, 10]
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
