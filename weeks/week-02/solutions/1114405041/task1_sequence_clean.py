"""Task 1: Sequence Clean."""

from __future__ import annotations


def parse_numbers(text: str) -> list[int]:
	if not text.strip():
		return []
	return [int(x) for x in text.split()]


def dedupe_keep_order(numbers: list[int]) -> list[int]:
	seen: set[int] = set()
	out: list[int] = []
	for num in numbers:
		if num not in seen:
			seen.add(num)
			out.append(num)
	return out


def format_line(label: str, values: list[int]) -> str:
	return f"{label}: {' '.join(map(str, values))}" if values else f"{label}:"


def solve(text: str) -> str:
	numbers = parse_numbers(text)

	dedupe = dedupe_keep_order(numbers)
	asc = sorted(numbers)
	desc = sorted(numbers, reverse=True)
	evens = [x for x in numbers if x % 2 == 0]

	lines = [
		format_line("dedupe", dedupe),
		format_line("asc", asc),
		format_line("desc", desc),
		format_line("evens", evens),
	]
	return "\n".join(lines)


DEFAULT_SAMPLE_INPUT = "5 3 5 2 9 2 8 3 1\n"


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
