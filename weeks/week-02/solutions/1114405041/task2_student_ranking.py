"""Task 2: Student Ranking."""

from __future__ import annotations


Student = tuple[str, int, int]


def parse_input(text: str) -> tuple[int, list[Student]]:
	lines = [line.strip() for line in text.splitlines() if line.strip()]
	if not lines:
		return 0, []

	n, k = map(int, lines[0].split())
	students: list[Student] = []
	for row in lines[1 : 1 + n]:
		name, score, age = row.split()
		students.append((name, int(score), int(age)))

	return k, students


def rank_students(students: list[Student], k: int) -> list[Student]:
	ranked = sorted(students, key=lambda s: (-s[1], s[2], s[0]))
	return ranked[:k]


def solve(text: str) -> str:
	k, students = parse_input(text)
	ranked = rank_students(students, k)
	return "\n".join(f"{name} {score} {age}" for name, score, age in ranked)


DEFAULT_SAMPLE_INPUT = """6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
"""


def read_input_data() -> str:
	import sys

	if sys.stdin.isatty():
		return DEFAULT_SAMPLE_INPUT

	data = sys.stdin.read()
	return data if data.strip() else DEFAULT_SAMPLE_INPUT


def main() -> None:
	data = read_input_data()
	print(solve(data))


if __name__ == "__main__":
	main()
