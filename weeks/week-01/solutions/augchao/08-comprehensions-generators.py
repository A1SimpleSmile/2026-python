# 8 容器操作與推導式範例
# ===========================================
# 本文件演示Python中最重要的三種推導式(Comprehension)和生成器表達式

# ◆ 範例1：列表推導式 (List Comprehension)
# 快速建立新列表的方式，可以過濾和轉換元素
nums = [1, -2, 3, -4]  # 初始列表，包含正數和負數

# 使用列表推導式提取所有正數
# 語法：[表達式 for 變數 in 序列 if 條件]
# 作用：遍歷nums中的每個元素n，只保留n > 0的元素
positives = [n for n in nums if n > 0]

print(positives)  # [1, 3] - 輸出結果：只有正數1和3

# ◆ 範例2：字典推導式 (Dictionary Comprehension)
# 快速建立新字典的方式，通常用於鍵值對的轉換
pairs = [('a', 1), ('b', 2)]  # 包含元組(鍵, 值)的列表

# 使用字典推導式將元組列表轉換為字典
# 語法：{鍵表達式: 值表達式 for 變數 in 序列}
# 作用：遍歷pairs中的每個元組(k, v)，k成為鍵，v成為值
lookup = {k: v for k, v in pairs}

print(lookup)  # {'a': 1, 'b': 2} - 輸出結果：轉換後的字典

# ◆ 範例3：生成器表達式 (Generator Expression)
# 與列表推導式類似，但使用圓括號()而非方括號[]
# 優點：節省記憶體，不會一次性建立所有元素，而是按需產生

# 計算列表中所有數字平方和
# 語法：(表達式 for 變數 in 序列)
# 作用：逐個產生nums中元素的平方，sum()將它們累加
squares_sum = sum(n * n for n in nums)

print(squares_sum)  # 30 - 說明：1² + (-2)² + 3² + (-4)² = 1 + 4 + 9 + 16 = 30