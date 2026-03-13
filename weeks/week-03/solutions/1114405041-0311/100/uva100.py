"""UVA 100 - The 3n + 1 problem

此版本使用記憶化（memoization）加速 cycle-length 計算，
適合大量區間查詢或較大的測資。
"""

from __future__ import annotations

from typing import Dict


def cycle_length(n: int, cache: Dict[int, int]) -> int:
    """計算 n 的 cycle-length（包含 n 與 1）。

    參數:
    - n: 欲計算的正整數
    - cache: 已計算過的長度快取，避免重複遞迴/迴圈運算
    """
    original = n
    path: list[int] = []

    # 一路往下推進，直到碰到快取中的值為止。
    while n not in cache:
        path.append(n)
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2

    # base_len 是目前 n（已在 cache）對應的 cycle-length。
    base_len = cache[n]

    # 反向回填剛剛走過的路徑，讓後續查詢可 O(1) 取得。
    for value in reversed(path):
        base_len += 1
        cache[value] = base_len

    return cache[original]


def max_cycle_length(i: int, j: int, cache: Dict[int, int] | None = None) -> int:
    """回傳區間 [i, j]（含端點）中最大的 cycle-length。"""
    if cache is None:
        cache = {1: 1}

    left, right = (i, j) if i <= j else (j, i)
    best = 0

    for n in range(left, right + 1):
        best = max(best, cycle_length(n, cache))

    return best


def solve(text: str) -> str:
    """解析多行輸入，輸出 UVA 指定格式字串。"""
    cache: Dict[int, int] = {1: 1}
    output_lines: list[str] = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        i_str, j_str = line.split()
        i, j = int(i_str), int(j_str)
        answer = max_cycle_length(i, j, cache)
        output_lines.append(f"{i} {j} {answer}")

    return "\n".join(output_lines)


def read_input_data() -> str:
    """優先讀 stdin；若沒有資料則進入互動輸入模式。"""
    import sys

    data = sys.stdin.read()
    if data:
        return data

    print("請貼上輸入資料，單獨一行輸入 EOF 結束：")
    lines: list[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "EOF":
            break
        lines.append(line)

    return "\n".join(lines)


def main() -> None:
    """程式進入點：讀 stdin，印出結果。"""
    data = read_input_data()
    if data:
        print(solve(data))


if __name__ == "__main__":
    main()
