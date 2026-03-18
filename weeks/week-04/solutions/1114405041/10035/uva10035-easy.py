"""UVA 10035 - Primary Arithmetic（簡單版）

思路：
1. 從個位開始，每位相加（含前一位進位）
2. 若總和 >= 10 → 本次產生進位，carry = 1，計數 +1
3. 重複直到兩個數都歸零且無進位
4. 依計數輸出對應文字（注意 operation 單複數）

口訣：「個位加，滿十進，數進位次」

常見陷阱：
- operation vs operations（1 次無 s，多次有 s）
- 進位本身也可能在最高位再次產生進位（例如 9 + 1 = 10，要再進一次）
"""

from __future__ import annotations


def carries(a: int, b: int) -> int:
    """模擬直式加法，回傳進位總次數。"""
    carry = 0   # 上一位帶下來的進位
    cnt = 0     # 進位計數

    while a or b or carry:           # 還有位數或進位就繼續
        s = a % 10 + b % 10 + carry  # 當前個位相加（含進位）
        carry = s // 10              # 新進位（結果>=10時才為1）
        if carry:
            cnt += 1                 # 本次有進位，計數加一
        a //= 10                     # 去掉個位
        b //= 10

    return cnt


def solve(text: str) -> str:
    """逐行讀取兩個數相加，輸出進位說明。"""
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:          # 遇到 "0 0" 停止
            break
        c = carries(a, b)
        # 依進位次數決定輸出格式（注意 1 次和多次的差異）
        if c == 0:
            out.append("No carry operation.")
        elif c == 1:
            out.append("1 carry operation.")
        else:
            out.append(f"{c} carry operations.")
    return "\n".join(out)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
