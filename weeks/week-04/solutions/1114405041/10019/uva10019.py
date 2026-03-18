"""UVA 10019 - Hashmat the Brave Warrior

Hashmat 將領想知道己方與敵方士兵數的差距，以決定是否開戰。
每行給定兩個整數（誰先誰後不確定），輸出兩數差的絕對值。

注意：題目說數字「不超過 2^63」，在 C 語言需要 unsigned long long，
但 Python 的整數沒有上限，直接 abs(a - b) 即可。
輸入無終止條件，讀到 EOF 為止。
"""

from __future__ import annotations


def solve(text: str) -> str:
    """逐行讀取兩個整數，輸出兩者差的絕對值。

    參數:
    - text: 多行輸入字串，每行包含兩個整數

    回傳:
    - 每行對應一個差值結果，以換行符分隔
    """
    out: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:       # 跳過空行
            continue
        a, b = map(int, line.split())
        out.append(str(abs(a - b)))    # Python 整數可直接處理巨大數字
    return "\n".join(out)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
