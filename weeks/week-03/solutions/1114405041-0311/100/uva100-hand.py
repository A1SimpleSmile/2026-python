"""UVA 100 hand version"""

from __future__ import annotations


def cycle_length(n: int) -> int:
    cnt = 1
    while n != 1:
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n //= 2
        cnt += 1
    return cnt


def max_cycle(i: int, j: int) -> int:
    if i > j:
        i, j = j, i

    best = 0
    for x in range(i, j + 1):
        best = max(best, cycle_length(x))
    return best


def solve(text: str) -> str:
    out: list[str] = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        out.append(f"{a} {b} {max_cycle(a, b)}")

    return "\n".join(out)


TEST_INPUT = """1 10
100 200
201 210
900 1000
"""


def main() -> None:
    print(solve(TEST_INPUT))


if __name__ == "__main__":
    main()
