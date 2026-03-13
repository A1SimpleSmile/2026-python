"""UVA 118 - 進階版（檔名保留 test）

這個檔案不是 unittest，而是較進階結構的解題程式：
- 用 dataclass 表示機器人狀態
- 封裝方向旋轉與前進邏輯
- 直接輸出題目經典範例結果
"""

from __future__ import annotations

from dataclasses import dataclass


ORDER = "NESW"
STEP = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


@dataclass
class Robot:
    x: int
    y: int
    d: str

    def turn_left(self) -> None:
        self.d = ORDER[(ORDER.index(self.d) - 1) % 4]

    def turn_right(self) -> None:
        self.d = ORDER[(ORDER.index(self.d) + 1) % 4]


def solve(text: str) -> str:
    """模擬所有機器人並回傳最終輸出。"""
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

        robot = Robot(int(x), int(y), d)
        lost = False

        for c in cmd:
            if c == "L":
                robot.turn_left()
                continue
            if c == "R":
                robot.turn_right()
                continue

            dx, dy = STEP[robot.d]
            nx, ny = robot.x + dx, robot.y + dy

            if nx < 0 or nx > limit_x or ny < 0 or ny > limit_y:
                if (robot.x, robot.y) in scent:
                    continue
                scent.add((robot.x, robot.y))
                lost = True
                break

            robot.x, robot.y = nx, ny

        if lost:
            out.append(f"{robot.x} {robot.y} {robot.d} LOST")
        else:
            out.append(f"{robot.x} {robot.y} {robot.d}")

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
    """直接輸出題目經典範例結果。"""
    print(solve(TEST_INPUT))


if __name__ == "__main__":
    main()
