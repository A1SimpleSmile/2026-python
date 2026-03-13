"""UVA 490 - 進階版（檔名保留 test）

這個檔案不是 unittest，而是較進階結構的解題程式：
- 使用類別封裝旋轉邏輯
- 清楚分離初始化與輸出流程
- 直接輸出題目示範結果
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SentenceRotator:
    lines: list[str]

    @property
    def width(self) -> int:
        """輸入矩陣的最大寬度。"""
        return max((len(s) for s in self.lines), default=0)

    def rotated_rows(self) -> list[str]:
        """產生旋轉後的每一列字串。"""
        out: list[str] = []

        for c in range(self.width):
            row_chars: list[str] = []
            for r in range(len(self.lines) - 1, -1, -1):
                if c < len(self.lines[r]):
                    row_chars.append(self.lines[r][c])
                else:
                    row_chars.append(" ")
            out.append("".join(row_chars).rstrip())

        return out


def solve(text: str) -> str:
    """把輸入內容順時針旋轉 90 度。"""
    rotator = SentenceRotator(text.splitlines())
    return "\n".join(rotator.rotated_rows())


TEST_INPUT = """HELLO
WORLD
"""


def main() -> None:
    """直接輸出題目示範輸入的旋轉結果。"""
    print(solve(TEST_INPUT))


if __name__ == "__main__":
    main()
