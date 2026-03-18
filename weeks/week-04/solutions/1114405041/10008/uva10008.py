"""UVA 10008 - What's Cryptanalysis?

統計輸入文字中每個英文字母出現的次數，
按照出現次數由多到少排列；次數相同時按字母順序（A→Z）輸出。
大小寫視為同一字母（a 和 A 都算 A）。
未出現的字母不輸出。
"""

from __future__ import annotations

from collections import Counter


def count_letters(lines: list[str]) -> Counter:
    """統計一組文字中每個英文字母（A-Z）的出現次數（不分大小寫）。

    參數:
    - lines: 要統計的文字行串列

    回傳:
    - Counter，鍵為大寫字母，值為出現次數
    """
    counts: Counter = Counter()
    for line in lines:
        for ch in line.upper():
            if ch.isalpha():  # 只計算英文字母，跳過數字與符號
                counts[ch] += 1
    return counts


def format_output(counts: Counter) -> str:
    """將計數結果依題目要求排序並格式化為輸出字串。

    排序規則：
    - 主鍵：出現次數由大到小（降冪）
    - 次鍵：字母由小到大（升冪），處理次數相同的情況
    """
    # lambda 回傳 tuple：(-次數, 字母)，Python 依序比較 tuple 元素
    sorted_chars = sorted(counts.keys(), key=lambda c: (-counts[c], c))
    return "\n".join(f"{c} {counts[c]}" for c in sorted_chars)


def solve(text: str) -> str:
    """解析輸入文字並輸出字母統計結果。

    輸入格式：
    - 第一行：整數 n，代表接下來要分析幾行
    - 接下來 n 行：密文內容
    """
    lines = text.splitlines()
    if not lines:
        return ""
    n = int(lines[0].strip())          # 讀取要分析的行數
    content_lines = lines[1:n + 1]     # 取出要分析的 n 行
    counts = count_letters(content_lines)
    return format_output(counts)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
