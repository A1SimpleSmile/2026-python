# 8 容器操作與推導式範例

# 定義一個包含正負數的列表
nums = [1, -2, 3, -4]

# 列表推導式：從 nums 中篩選出大於 0 的元素，組成新列表
# 相當於過濾出正數
positives = [n for n in nums if n > 0]

# 定義鍵值對的列表
pairs = [('a', 1), ('b', 2)]

# 字典推導式：從 pairs 中創建字典
# 將每個元組的第一個元素作為鍵，第二個作為值
lookup = {k: v for k, v in pairs}

# 生成器表達式：創建一個生成器，對 nums 中的每個 n 計算 n*n
# 然後使用 sum() 函式計算所有平方的總和
# 生成器不會立即計算所有值，節省記憶體
squares_sum = sum(n * n for n in nums)

# 顯示結果
print("原始數字:", nums)
print("正數列表:", positives)
print("字典:", lookup)
print("平方和:", squares_sum)

# 額外示例：使用生成器進行其他操作
print("\n=== 額外示例 ===")

# 生成器可以用於其他函式
even_squares = [x * x for x in nums if x % 2 == 0]  # 偶數的平方
print("偶數的平方:", even_squares)

# 生成器表達式用於 max()
max_square = max(n * n for n in nums)
print("最大平方:", max_square)

# 生成器表達式轉成列表
squares_list = list(n * n for n in nums)
print("所有平方列表:", squares_list)

# 集合推導式（set comprehension）
unique_squares = {n * n for n in nums}
print("唯一平方集合:", unique_squares)

# 字典推導式的高級用法
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
name_score_dict = {name: score for name, score in zip(names, scores)}
print("姓名分數字典:", name_score_dict)

# 條件字典推導式
high_scores = {name: score for name, score in name_score_dict.items() if score > 80}
print("高分學生:", high_scores)
