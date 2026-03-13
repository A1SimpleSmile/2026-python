"""UVA 490 hand version"""

from __future__ import annotations


def solve(text: str) -> str:
    lines = text.splitlines()
    if not lines:
        return ""

    width = max(len(s) for s in lines)
    out: list[str] = []

    for c in range(width):
        row: list[str] = []
        for r in range(len(lines) - 1, -1, -1):
            if c < len(lines[r]):
                row.append(lines[r][c])
            else:
                row.append(" ")
        out.append("".join(row).rstrip())

    return "\n".join(out)


TEST_INPUT = """HELLO
WORLD
"""


def main() -> None:
    print(solve(TEST_INPUT))


if __name__ == "__main__":
    main()
