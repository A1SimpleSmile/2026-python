"""Task 3: Log Summary."""

from __future__ import annotations

from collections import Counter, defaultdict


def parse_input(text: str) -> list[tuple[str, str]]:
	lines = [line.strip() for line in text.splitlines() if line.strip()]
	if not lines:
		return []

	m = int(lines[0])
	logs: list[tuple[str, str]] = []
	for row in lines[1 : 1 + m]:
		user, action = row.split()
		logs.append((user, action))
	return logs


def summarize(logs: list[tuple[str, str]]) -> tuple[list[tuple[str, int]], tuple[str | None, int]]:
	user_counts: defaultdict[str, int] = defaultdict(int)
	action_counts: Counter[str] = Counter()

	for user, action in logs:
		user_counts[user] += 1
		action_counts[action] += 1

	users_sorted = sorted(user_counts.items(), key=lambda item: (-item[1], item[0]))

	if not action_counts:
		return users_sorted, (None, 0)

	max_count = max(action_counts.values())
	top_actions = sorted(a for a, c in action_counts.items() if c == max_count)
	return users_sorted, (top_actions[0], max_count)


def solve(text: str) -> str:
	logs = parse_input(text)
	users_sorted, (top_action, top_count) = summarize(logs)

	lines = [f"{user} {count}" for user, count in users_sorted]
	lines.append(f"top_action: {top_action if top_action is not None else 'None'} {top_count}")
	return "\n".join(lines)


DEFAULT_SAMPLE_INPUT = """8
alice login
bob login
alice view
alice logout
bob view
bob view
chris login
bob logout
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
