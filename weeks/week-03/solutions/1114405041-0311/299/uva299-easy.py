"""UVA 299 - easy 簡單版

題意要找最少相鄰交換次數，等價於反轉數。
這版用雙層迴圈，直接數反轉，最容易看懂。
"""

from __future__ import annotations


def count_inversions(arr: list[int]) -> int:
    """用 O(n^2) 直接數反轉對。"""
    inv = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv


def solve(text: str) -> str:
    """依題目輸入格式產生輸出。"""
    parts = text.split()
    if not parts:
        return ""

    p = 0
    t = int(parts[p])
    p += 1
    out: list[str] = []

    for _ in range(t):
        l = int(parts[p])
        p += 1
        train = list(map(int, parts[p : p + l]))
        p += l
        out.append(f"Optimal train swapping takes {count_inversions(train)} swaps.")

    return "\n".join(out)


TEST_INPUT = """3
3
1 3 2
4
4 3 2 1
5
1 2 3 4 5
"""


def main() -> None:
    """直接輸出題目型態的範例結果。"""
    print(solve(TEST_INPUT))


if __name__ == "__main__":
    main()
