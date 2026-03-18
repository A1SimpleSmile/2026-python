"""UVA 10035 - Primary Arithmetic

模擬直式加法，計算兩個非負整數相加時發生的進位（carry）次數。

直式加法規則：從個位開始，每位相加若 >= 10 就產生進位，
進位加到高一位，直到所有位數和進位都歸零。

輸入格式：每行兩個非負整數，最後一行為 0 0 結束輸入。
輸出格式：
  - 0 次進位 → "No carry operation."
  - 1 次進位 → "1 carry operation."        （注意無複數 s）
  - n 次進位 → "n carry operations."       （注意有複數 s）
"""

from __future__ import annotations


def count_carries(a: int, b: int) -> int:
    """計算 a + b 的直式加法中發生進位的次數。

    做法：從個位開始逐位相加，
    若（本位數字之和 + 進位）>= 10，則新進位 = 1，計數 +1。

    參數:
    - a, b: 兩個非負整數

    回傳:
    - 進位次數（整數）
    """
    carry = 0   # 從上一位帶來的進位（0 或 1）
    count = 0   # 累計進位次數

    # 只要 a、b 還有位數，或還有未處理的進位，就繼續
    while a > 0 or b > 0 or carry > 0:
        digit_sum = (a % 10) + (b % 10) + carry  # 當前個位相加（含進位）
        carry = digit_sum // 10                   # 新的進位值（0 或 1）
        if carry:
            count += 1   # 產生進位，次數 +1
        a //= 10         # 去掉個位，移到十位
        b //= 10

    return count


def format_carry(count: int) -> str:
    """依題目格式將進位次數轉為輸出字串。

    注意英文單複數規則：
    - 0 次：No carry operation.
    - 1 次：1 carry operation.    （operation 無 s）
    - 多次：n carry operations.   （operation 加 s）
    """
    if count == 0:
        return "No carry operation."
    elif count == 1:
        return "1 carry operation."
    else:
        return f"{count} carry operations."


def solve(text: str) -> str:
    """解析輸入並對每組資料輸出進位說明。"""
    out: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:   # "0 0" 代表輸入結束，不處理
            break
        out.append(format_carry(count_carries(a, b)))
    return "\n".join(out)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
