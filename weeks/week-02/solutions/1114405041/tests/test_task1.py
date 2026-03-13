"""Task 1 單元測試：Sequence Clean。"""

from __future__ import annotations

import pathlib
import sys
import unittest


BASE = pathlib.Path(__file__).resolve().parent.parent
if str(BASE) not in sys.path:
	sys.path.insert(0, str(BASE))

import task1_sequence_clean as t1


class TestTask1SequenceClean(unittest.TestCase):
	def test_sample_output(self):
		data = "5 3 5 2 9 2 8 3 1"
		expected = """dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8"""
		self.assertEqual(t1.solve(data), expected)

	def test_empty_input(self):
		expected = """dedupe:
asc:
desc:
evens:"""
		self.assertEqual(t1.solve(""), expected)

	def test_order_preserving_dedupe(self):
		nums = [2, 1, 2, 3, 1, 4]
		self.assertEqual(t1.dedupe_keep_order(nums), [2, 1, 3, 4])


if __name__ == "__main__":
	unittest.main(verbosity=2)
