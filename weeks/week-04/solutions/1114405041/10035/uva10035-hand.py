"""UVA 10035 hand version"""

from __future__ import annotations


def solve(text: str) -> str:
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        carry = 0
        count = 0
        while a > 0 or b > 0 or carry > 0:
            s = a % 10 + b % 10 + carry
            carry = s // 10
            if carry:
                count += 1
            a //= 10
            b //= 10
        if count == 0:
            out.append("No carry operation.")
        elif count == 1:
            out.append("1 carry operation.")
        else:
            out.append(f"{count} carry operations.")
    return "\n".join(out)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))
