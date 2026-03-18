"""UVA 948 hand version"""

from __future__ import annotations


def _fits(coin: int, weighings: list, lighter: bool) -> bool:
    for left, right, result in weighings:
        if result == '=':
            if coin in left or coin in right:
                return False
        elif result == '<':
            if lighter:
                if coin not in left:
                    return False
            else:
                if coin not in right:
                    return False
        else:
            if lighter:
                if coin not in right:
                    return False
            else:
                if coin not in left:
                    return False
    return True


def solve(text: str) -> str:
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    idx = 0
    M = int(lines[idx]); idx += 1
    results = []
    for _ in range(M):
        N, K = map(int, lines[idx].split()); idx += 1
        weighings = []
        for _ in range(K):
            parts = list(map(int, lines[idx].split())); idx += 1
            result = lines[idx]; idx += 1
            Pi = parts[0]
            left  = set(parts[1:Pi + 1])
            right = set(parts[Pi + 1:2 * Pi + 1])
            weighings.append((left, right, result))
        candidates = [
            c for c in range(1, N + 1)
            if _fits(c, weighings, True) or _fits(c, weighings, False)
        ]
        results.append(str(candidates[0] if len(candidates) == 1 else 0))
    return "\n\n".join(results)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
