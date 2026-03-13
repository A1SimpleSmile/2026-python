"""Task 2 單元測試：Student Ranking。"""

from __future__ import annotations

import pathlib
import sys
import unittest


BASE = pathlib.Path(__file__).resolve().parent.parent
if str(BASE) not in sys.path:
	sys.path.insert(0, str(BASE))

import task2_student_ranking as t2


class TestTask2StudentRanking(unittest.TestCase):
	def test_sample_output(self):
		data = """6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
"""
		expected = """eva 92 20
zoe 92 21
bob 88 19"""
		self.assertEqual(t2.solve(data), expected)

	def test_tie_break_age_then_name(self):
		students = [
			("amy", 88, 19),
			("bob", 88, 19),
			("zoe", 88, 20),
		]
		ranked = t2.rank_students(students, 3)
		self.assertEqual(ranked, [("amy", 88, 19), ("bob", 88, 19), ("zoe", 88, 20)])

	def test_k_larger_than_n(self):
		data = """2 5
tom 90 20
amy 80 19
"""
		expected = """tom 90 20
amy 80 19"""
		self.assertEqual(t2.solve(data), expected)


if __name__ == "__main__":
	unittest.main(verbosity=2)
