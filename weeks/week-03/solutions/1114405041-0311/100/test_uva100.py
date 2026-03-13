"""UVA 100 - 進階版（檔名保留 test）

這個檔案不是 unittest，而是較進階的解題程式：
- 使用快取（memoization）
- 保留清楚函式分層
- 直接輸出題目範例對應結果
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CollatzSolver:
    """可重複使用的 Collatz 計算器。"""

    cache: dict[int, int] = field(default_factory=lambda: {1: 1})

    def cycle_length(self, n: int) -> int:
        """回傳 n 的 cycle length，並把中間結果寫回快取。"""
        origin = n
        path: list[int] = []

        while n not in self.cache:
            path.append(n)
            if n % 2 == 1:
                n = 3 * n + 1
            else:
                n //= 2

        length = self.cache[n]
        for value in reversed(path):
            length += 1
            self.cache[value] = length

        return self.cache[origin]

    def max_cycle(self, i: int, j: int) -> int:
        """計算區間 [i, j] 的最大 cycle length。"""
        if i > j:
            i, j = j, i

        best = 0
        for x in range(i, j + 1):
            best = max(best, self.cycle_length(x))
        return best


def solve(text: str) -> str:
    """依題目格式輸出 `i j answer`。"""
    engine = CollatzSolver()
    out: list[str] = []

    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        i, j = map(int, line.split())
        out.append(f"{i} {j} {engine.max_cycle(i, j)}")

    return "\n".join(out)


TEST_INPUT = """1 10
100 200
201 210
900 1000
"""


def main() -> None:
    """直接輸出題目範例結果。"""
    print(solve(TEST_INPUT))


if __name__ == "__main__":
    main()
