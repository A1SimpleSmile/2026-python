"""UVA 10008 - What's Cryptanalysis?（簡單版）

思路：
1. 讀第一行的數字 n，知道要分析幾行
2. 對每行的每個字元，若是英文字母就轉大寫、計數加一
3. 依「次數大→小」再「字母 A→Z」排序後輸出

口訣：「逐字計數，大數優先，同數按序」
"""

from __future__ import annotations


def solve(text: str) -> str:
    """從多行文字中統計字母並輸出排序結果。"""
    lines = text.splitlines()
    n = int(lines[0])       # 第一行：要分析幾行文字

    count = {}              # 字典：大寫字母 → 出現次數

    # 逐行、逐字元統計（只處理英文字母）
    for line in lines[1:n + 1]:
        for ch in line.upper():
            if ch.isalpha():                        # 只計英文字母
                count[ch] = count.get(ch, 0) + 1   # 沒出現過就從 0 開始

    # 排序：次數由大到小，次數相同時字母由小到大
    # sorted() 的 key 回傳 (-次數, 字母)，Python 會逐欄比較
    result = sorted(count, key=lambda c: (-count[c], c))

    # 組合輸出：每行「字母 次數」
    out = []
    for c in result:
        out.append(f"{c} {count[c]}")

    return "\n".join(out)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
