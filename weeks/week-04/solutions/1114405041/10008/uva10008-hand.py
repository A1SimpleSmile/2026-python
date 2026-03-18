"""UVA 10008 hand version"""

from __future__ import annotations


def solve(text: str) -> str:
    lines = text.splitlines()
    n = int(lines[0])
    count = {}
    for line in lines[1:n + 1]:
        for ch in line.upper():
            if ch.isalpha():
                count[ch] = count.get(ch, 0) + 1
    result = sorted(count, key=lambda c: (-count[c], c))
    return "\n".join(f"{c} {count[c]}" for c in result)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
