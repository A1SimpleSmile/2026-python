"""UVA 490 - easy 簡單版

做法：
1. 找最長行長度
2. 逐欄由下往上讀
3. 不存在的位置補空白
"""

from __future__ import annotations


def solve(text: str) -> str:
    """把輸入句子順時針旋轉 90 度。"""
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
    """直接輸出題目示範輸入的旋轉結果。"""
    print(solve(TEST_INPUT))


if __name__ == "__main__":
    main()
