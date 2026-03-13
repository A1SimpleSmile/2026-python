"""UVA 299 - 進階版（檔名保留 test）

這個檔案不是 unittest，而是進階解題版本：
- 使用 merge sort 計算反轉數
- 時間複雜度 O(n log n)
- 直接輸出題目格式結果
"""

from __future__ import annotations


def merge_count(arr: list[int]) -> tuple[list[int], int]:
    """回傳排序後陣列與反轉數。"""
    n = len(arr)
    if n <= 1:
        return arr[:], 0

    mid = n // 2
    left_sorted, left_inv = merge_count(arr[:mid])
    right_sorted, right_inv = merge_count(arr[mid:])

    merged: list[int] = []
    i = j = 0
    cross_inv = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            cross_inv += len(left_sorted) - i
            j += 1

    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])

    return merged, left_inv + right_inv + cross_inv


def solve(text: str) -> str:
    """依題目格式解析並輸出每組答案。"""
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
        _, inv = merge_count(train)
        out.append(f"Optimal train swapping takes {inv} swaps.")

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
