"""UVA 10019 - Hashmat the Brave Warrior（簡單版）

思路超簡單：
1. 每行讀兩個數字 a 和 b
2. 輸出 abs(a - b)，即兩者差的正整數

關鍵：Python 的 int 沒有上限，不需要特別處理 2^63 的大數，
直接 abs(a - b) 就能得到正確答案。
"""

from __future__ import annotations


def solve(text: str) -> str:
    """讀取多行輸入，每行輸出兩個數的差（正整數）。"""
    out = []
    for line in text.split("\n"):      # 逐行處理
        line = line.strip()
        if not line:                   # 跳過空行（EOF 前可能有空白）
            continue
        a, b = map(int, line.split())  # 讀取兩個整數（不管誰先誰後）
        out.append(str(abs(a - b)))    # 絕對值差，保證輸出正整數
    return "\n".join(out)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
