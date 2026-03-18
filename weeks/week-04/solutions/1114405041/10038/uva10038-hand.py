"""UVA 10038 hand version"""

from __future__ import annotations


def solve(text: str) -> str:
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        nums = list(map(int, line.split()))
        n = nums[0]
        seq = nums[1:]
        if n == 1:
            out.append("Jolly")
            continue
        diffs = set(abs(seq[i] - seq[i - 1]) for i in range(1, n))
        if diffs == set(range(1, n)):
            out.append("Jolly")
        else:
            out.append("Not jolly")
    return "\n".join(out)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
