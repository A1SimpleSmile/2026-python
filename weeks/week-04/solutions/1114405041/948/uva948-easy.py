"""UVA 948 - Fake Coin（簡單版）

思路：
逐一試每枚幣是不是假幣，用兩個問題篩選：
  Q1：它有沒有辦法是「較輕」假幣？
  Q2：它有沒有辦法是「較重」假幣？

判斷假幣是「較輕」的條件（只要有一個矛盾就排除）：
  ・天平 = ：假幣不能在場（否則秤重會不平衡，矛盾）
  ・天平 < （左輕）：假幣必須在左邊（輕的那側），不在左就矛盾
  ・天平 > （右輕）：假幣必須在右邊（輕的那側），不在右就矛盾

「較重」同理，只是左右互換。

最後：剛好只有一枚幣符合任一條件 → 那就是假幣；否則輸出 0。

輸入解析技巧：把所有空行過濾掉，簡化 index 計算。
"""

from __future__ import annotations


def _fits(coin: int, weighings: list, lighter: bool) -> bool:
    """檢查 coin 是否符合「較輕」（lighter=True）或「較重」（lighter=False）假幣的所有秤重記錄。"""
    for left, right, result in weighings:
        if result == '=':
            if coin in left or coin in right:
                return False        # 平衡時假幣不能在場
        elif result == '<':         # 左輕右重
            if lighter:
                if coin not in left:
                    return False    # 輕假幣應在左（輕的那側）
            else:
                if coin not in right:
                    return False    # 重假幣應在右（重的那側）
        else:                       # '>' 左重右輕
            if lighter:
                if coin not in right:
                    return False    # 輕假幣應在右（輕的那側）
            else:
                if coin not in left:
                    return False    # 重假幣應在左（重的那側）
    return True


def solve(text: str) -> str:
    """解析輸入並對每組測資找出假幣。"""
    # 過濾空行，簡化索引操作
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    idx = 0

    M = int(lines[idx]); idx += 1      # 測資組數
    results = []

    for _ in range(M):
        N, K = map(int, lines[idx].split()); idx += 1   # 硬幣數、秤重次數
        weighings = []

        for _ in range(K):
            # 解析硬幣排列：Pi L1..LPi R1..RPi
            parts = list(map(int, lines[idx].split())); idx += 1
            result = lines[idx]; idx += 1               # <、>、=

            Pi    = parts[0]                             # 每邊放幾個
            left  = set(parts[1 : Pi + 1])               # 左邊集合
            right = set(parts[Pi + 1 : 2 * Pi + 1])      # 右邊集合
            weighings.append((left, right, result))

        # 找出所有符合條件的候選硬幣
        candidates = [
            c for c in range(1, N + 1)
            if _fits(c, weighings, lighter=True) or _fits(c, weighings, lighter=False)
        ]

        # 恰好一枚候選才能確定是假幣
        results.append(str(candidates[0] if len(candidates) == 1 else 0))

    # 測資間輸出空行
    return "\n\n".join(results)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
