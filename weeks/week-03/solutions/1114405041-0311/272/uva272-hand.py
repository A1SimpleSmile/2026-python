"""UVA 272 - TEX Quotes（手打版本）"""

from __future__ import annotations


def solve(text: str) -> str:
   
    left = True
    ans: list[str] = []

    for c in text:
        if c == '"':
            if left:
                ans.append("``")
            else:
                ans.append("''")
            left = not left
        else:
            ans.append(c)

    return "".join(ans)


TEST_INPUT = '"To be or not to be," quoth the bard, "that is the question."\n'


def main() -> None:
    
    print(solve(TEST_INPUT), end="")


if __name__ == "__main__":
    main()
