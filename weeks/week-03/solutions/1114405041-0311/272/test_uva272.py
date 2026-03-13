"""UVA 272 - TEX Quotes（進階版，檔名保留 test）

注意：
- 這個檔案不是 unittest 測試器，而是「較進階寫法」的解題程式。
- 目的為：和 easy 版本同功能，但程式結構更完整。
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class QuoteTransformer:
    """維護引號狀態的轉換器。

    `is_opening=True` 代表下一個遇到的 `"` 應轉為 ``。
    轉換後會自動切換狀態，以符合題目「交替替換」規則。
    """

    is_opening: bool = True

    def convert_char(self, ch: str) -> str:
        """轉換單一字元；非雙引號原樣回傳。"""
        if ch != '"':
            return ch

        if self.is_opening:
            self.is_opening = False
            return "``"

        self.is_opening = True
        return "''"


def solve(text: str) -> str:
    """將輸入中的一般雙引號轉為 TeX 方向引號。"""
    transformer = QuoteTransformer()
    out: list[str] = []

    for ch in text:
        out.append(transformer.convert_char(ch))

    return "".join(out)


# 題目經典範例測資：直接執行即可看到輸出。
TEST_INPUT = '"To be or not to be," quoth the bard, "that is the question."\n'


def main() -> None:
    """直接使用程式內測資，輸出轉換結果。"""
    print(solve(TEST_INPUT), end="")


if __name__ == "__main__":
    main()
