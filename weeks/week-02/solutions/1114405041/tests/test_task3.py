"""Task 3 單元測試：Log Summary。"""

from __future__ import annotations

import pathlib
import sys
import unittest


BASE = pathlib.Path(__file__).resolve().parent.parent
if str(BASE) not in sys.path:
	sys.path.insert(0, str(BASE))

import task3_log_summary as t3


class TestTask3LogSummary(unittest.TestCase):
	def test_sample_output(self):
		data = """8
alice login
bob login
alice view
alice logout
bob view
bob view
chris login
bob logout
"""
		expected = """bob 4
alice 3
chris 1
top_action: login 3"""
		self.assertEqual(t3.solve(data), expected)

	def test_empty_logs(self):
		expected = "top_action: None 0"
		self.assertEqual(t3.solve("0\n"), expected)

	def test_user_sort_tie_by_name(self):
		data = """4
bob login
amy view
bob logout
amy login
"""
		expected = """amy 2
bob 2
top_action: login 2"""
		self.assertEqual(t3.solve(data), expected)


if __name__ == "__main__":
	unittest.main(verbosity=2)
