"""UVA 948 - Fake Coin

在 N 個硬幣中找出唯一的假幣（重量異常，可能較輕或較重）。
利用天平秤重結果（<、>、=）逐一驗證每枚硬幣。

核心邏輯：對每枚候選幣，假設它是「較輕假幣」或「較重假幣」，
          檢查該假設是否與所有秤重結果一致，若恰好只有一枚符合則輸出。

「較輕假幣」一致性規則：
  - 結果 =：假幣不得出現（若出現代表它也被秤到了卻沒影響 → 矛盾）
  - 結果 <（左輕右重）：假幣必須在左邊（輕的那側）
  - 結果 >（左重右輕）：假幣必須在右邊（輕的那側）

「較重假幣」規則同理，只是換側。

若候選數 != 1，代表無法唯一確定，輸出 0。

輸入格式：
  第一行：M（測資組數），後跟空行
  每組：N K，然後 2K 行（每次秤重佔 2 行：硬幣排列 + 結果）
  測資間有空行
"""

from __future__ import annotations


def can_be_lighter(coin: int, weighings: list) -> bool:
    """判斷 coin 是否可能是「較輕」的假幣（與所有秤重結果一致）。

    規則（coin 若輕，它應在輕的那一側）：
    - 結果 =：coin 不應在場，否則矛盾
    - 結果 <（左輕）：coin 必須在左邊
    - 結果 >（右輕）：coin 必須在右邊
    """
    for left, right, result in weighings:
        if result == '=':
            if coin in left or coin in right:
                return False        # 平衡時假幣不應在場
        elif result == '<':
            if coin not in left:
                return False        # 假幣若輕，應在輕那側（左）
        else:                       # '>'
            if coin not in right:
                return False        # 假幣若輕，應在輕那側（右）
    return True


def can_be_heavier(coin: int, weighings: list) -> bool:
    """判斷 coin 是否可能是「較重」的假幣（與所有秤重結果一致）。

    規則（coin 若重，它應在重的那一側）：
    - 結果 =：coin 不應在場，否則矛盾
    - 結果 <（右重）：coin 必須在右邊
    - 結果 >（左重）：coin 必須在左邊
    """
    for left, right, result in weighings:
        if result == '=':
            if coin in left or coin in right:
                return False        # 平衡時假幣不應在場
        elif result == '<':
            if coin not in right:
                return False        # 假幣若重，應在重那側（右）
        else:                       # '>'
            if coin not in left:
                return False        # 假幣若重，應在重那側（左）
    return True


def find_fake(n: int, weighings: list) -> int:
    """在 1~N 號硬幣中找出假幣，無法唯一確定時回傳 0。"""
    candidates = [
        c for c in range(1, n + 1)
        if can_be_lighter(c, weighings) or can_be_heavier(c, weighings)
    ]
    return candidates[0] if len(candidates) == 1 else 0


def parse_input(text: str) -> list[tuple[int, list]]:
    """解析題目格式輸入，回傳各測資的 (N, weighings) 清單。

    注意：題目在測資間有空白行，這裡保留空行協助分隔。
    """
    lines = text.splitlines()   # 保留空行以正確跳過
    idx = 0

    # 跳過開頭的空行
    while idx < len(lines) and not lines[idx].strip():
        idx += 1

    M = int(lines[idx].strip())
    idx += 1

    cases = []
    for _ in range(M):
        # 跳過測資間的空行
        while idx < len(lines) and not lines[idx].strip():
            idx += 1
        if idx >= len(lines):
            break

        N, K = map(int, lines[idx].strip().split())
        idx += 1

        weighings = []
        for _ in range(K):
            # 解析硬幣排列行：Pi L1..LPi R1..RPi
            parts = list(map(int, lines[idx].strip().split()))
            idx += 1
            result = lines[idx].strip()     # 秤重結果：< > =
            idx += 1

            Pi = parts[0]                           # 每邊放幾個
            left  = set(parts[1 : Pi + 1])          # 左邊硬幣集合
            right = set(parts[Pi + 1 : 2 * Pi + 1]) # 右邊硬幣集合
            weighings.append((left, right, result))

        cases.append((N, weighings))
    return cases


def solve(text: str) -> str:
    """解析輸入、找每組假幣，測資間以空行分隔輸出。"""
    cases = parse_input(text)
    results = [str(find_fake(N, w)) for N, w in cases]
    return "\n\n".join(results)   # 題目要求測資間空一行


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
