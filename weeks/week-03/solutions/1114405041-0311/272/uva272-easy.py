"""UVA 272 - TEX Quotes（AI 簡單版）

這個 easy 版本刻意維持和手打版相同的執行模式：
1. 核心函式 `solve` 負責做引號替換
2. 直接執行時使用程式內測資 `TEST_INPUT`
3. 執行後立刻印出結果，方便課堂快速檢查
"""

from __future__ import annotations


TEST_INPUT = '"To be or not to be," quoth the bard, "that is the question."\n'


def solve(text: str) -> str:
    """將一般雙引號轉為 TeX 方向引號。"""
    opening = True
    out: list[str] = []

    for ch in text:
        # 題目保證雙引號會成對出現，所以只要交替替換即可。
        if ch == '"':
            if opening:
                out.append("``")
            else:
                out.append("''")
            opening = not opening
        else:
            out.append(ch)

    return "".join(out)


def main() -> None:
    """直接使用程式內測資，執行後立即輸出結果。"""
    print(solve(TEST_INPUT), end="")


if __name__ == "__main__":
    main()
