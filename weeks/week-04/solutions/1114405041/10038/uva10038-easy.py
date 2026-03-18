"""UVA 10038 - Jolly Jumpers（簡單版）

思路：
1. 每行第一個數是序列長度 n，後面才是序列
2. 算出 n-1 個相鄰差的絕對值，放進 set（集合）
3. 看 set 是否等於 {1, 2, ..., n-1}

為什麼用 set？
- set 自動去除重複 → 有重複差值時集合大小 < n-1
- 直接跟 set(range(1, n)) 比較，一行搞定

口訣：「差值集合，涵蓋 1 到 n-1，就是 Jolly」

長度為 1 的序列：沒有相鄰差，特例直接回傳 Jolly。
"""

from __future__ import annotations


def solve(text: str) -> str:
    """逐行判斷序列是否為 Jolly Jumper。"""
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        nums = list(map(int, line.split()))  # 整行轉整數串列
        n = nums[0]                          # 第一個數是序列長度
        seq = nums[1:]                       # 後面才是序列本身

        if n == 1:                           # 長度 1：題目定義為 Jolly
            out.append("Jolly")
            continue

        # 用 set comprehension 一次計算所有相鄰差的絕對值集合
        diffs = set(abs(seq[i] - seq[i - 1]) for i in range(1, n))

        # 只要集合等於 {1, 2, ..., n-1} 就是 Jolly
        if diffs == set(range(1, n)):
            out.append("Jolly")
        else:
            out.append("Not jolly")

    return "\n".join(out)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
