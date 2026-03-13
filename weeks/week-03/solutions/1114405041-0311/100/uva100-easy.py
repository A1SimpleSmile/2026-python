"""UVA 100 - The 3n + 1 problem（easy 簡單版）

這版主打：
1. 結構短
2. 變數少
3. 直接看得懂
"""

from __future__ import annotations


def cycle_length(n: int) -> int:
    """計算單一數字的 cycle length。"""
    cnt = 1
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2
        cnt += 1
    return cnt


def max_cycle(i: int, j: int) -> int:
    """找區間內最大 cycle length。"""
    if i > j:
        i, j = j, i

    best = 0
    for x in range(i, j + 1):
        best = max(best, cycle_length(x))
    return best


def solve(text: str) -> str:
    """依題目格式處理多行輸入。"""
    out: list[str] = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        out.append(f"{a} {b} {max_cycle(a, b)}")

    return "\n".join(out)


# 題目常見測資
TEST_INPUT = """1 10
100 200
201 210
900 1000
"""


def main() -> None:
    """直接執行時，印出題目範例結果。"""
    print(solve(TEST_INPUT))


if __name__ == "__main__":
    main()
