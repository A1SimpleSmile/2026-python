"""UVA 10038 - Jolly Jumpers

判斷一個長度為 n 的整數序列是否為「Jolly Jumper」。

定義：若序列中相鄰兩數差的絕對值集合恰好等於 {1, 2, ..., n-1}，
      則稱此序列為 Jolly Jumper。

例如：
  1 4 2 3  → 差的絕對值為 3, 2, 1 → 集合 {1,2,3} = {1~3} → Jolly
  1 4 2 -1 6 → 差為 3, 2, 3, 7 → 集合 {2,3,7} ≠ {1~4} → Not jolly

輸入格式：每行第一個數為 n（序列長度），後跟 n 個整數。
輸出格式：每行輸出 "Jolly" 或 "Not jolly"。
"""

from __future__ import annotations


def is_jolly(nums: list[int]) -> bool:
    """判斷整數串列是否為 Jolly Jumper。

    做法：
    1. 計算每對相鄰元素差的絕對值，收集成集合
    2. 比較集合是否等於 {1, 2, ..., n-1}
       - 集合天然去重複，並可直接比較是否完整涵蓋每個差值

    參數:
    - nums: 整數串列

    回傳:
    - True 表示 Jolly，False 表示 Not jolly
    """
    n = len(nums)
    if n == 1:
        return True    # 長度 1 的序列：無相鄰關係，題目定義為 Jolly

    # 收集所有相鄰差的絕對值
    diffs = set()
    for i in range(1, n):
        d = abs(nums[i] - nums[i - 1])
        diffs.add(d)

    # 集合大小若 < n-1，代表有重複或缺失；大小若 > n-1 不可能（只有 n-1 個差值）
    return diffs == set(range(1, n))


def solve(text: str) -> str:
    """解析每行輸入，輸出 'Jolly' 或 'Not jolly'。"""
    out: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = list(map(int, line.split()))
        n = parts[0]            # 序列長度
        nums = parts[1:n + 1]   # 序列本身
        out.append("Jolly" if is_jolly(nums) else "Not jolly")
    return "\n".join(out)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
