"""UVA 118 hand version"""

from __future__ import annotations


ORDER = "NESW"
STEP = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def solve(text: str) -> str:
    rows = [line.strip() for line in text.splitlines() if line.strip()]
    if not rows:
        return ""

    limit_x, limit_y = map(int, rows[0].split())
    scent: set[tuple[int, int]] = set()
    out: list[str] = []

    i = 1
    while i + 1 < len(rows):
        x, y, d = rows[i].split()
        cmd = rows[i + 1]
        i += 2

        px, py = int(x), int(y)
        lost = False

        for c in cmd:
            if c == "L":
                d = ORDER[(ORDER.index(d) - 1) % 4]
            elif c == "R":
                d = ORDER[(ORDER.index(d) + 1) % 4]
            else:
                dx, dy = STEP[d]
                nx, ny = px + dx, py + dy

                if nx < 0 or nx > limit_x or ny < 0 or ny > limit_y:
                    if (px, py) in scent:
                        continue
                    scent.add((px, py))
                    lost = True
                    break

                px, py = nx, ny

        if lost:
            out.append(f"{px} {py} {d} LOST")
        else:
            out.append(f"{px} {py} {d}")

    return "\n".join(out)


TEST_INPUT = """5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
"""


def main() -> None:
    print(solve(TEST_INPUT))


if __name__ == "__main__":
    main()
