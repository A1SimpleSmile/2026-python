"""UVA 10038 - 單元測試

測試 Jolly Jumpers 問題，重點驗證：
- 正確的 Jolly 序列（差值恰好涵蓋 1~n-1）
- 有重複差值（集合大小不足）→ Not jolly
- 差值超出範圍 → Not jolly
- 長度為 1 的邊界情況
- 含負數的序列
"""

import unittest
import importlib.util
import pathlib

BASE = pathlib.Path(__file__).parent


def _load(filename: str):
    """以絕對路徑載入 Python 模組，支援檔名含 - 的情況。"""
    name = filename.replace(".py", "").replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, BASE / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


std  = _load("uva10038.py")
easy = _load("uva10038-easy.py")
hand = _load("uva10038-hand.py")


class TestUVA10038(unittest.TestCase):

    def test_jolly_example(self):
        """題目範例：1 4 2 3 差的絕對值為 3,2,1 → Jolly。"""
        self.assertEqual(std.solve("4 1 4 2 3"), "Jolly")

    def test_not_jolly_example(self):
        """題目範例：1 4 2 -1 6 差的絕對值為 3,2,3,7 → Not jolly。"""
        self.assertEqual(std.solve("5 1 4 2 -1 6"), "Not jolly")

    def test_single_element(self):
        """長度為 1 的序列沒有相鄰差，題目定義為 Jolly。"""
        self.assertEqual(std.solve("1 42"), "Jolly")

    def test_length_two_jolly(self):
        """長度為 2：差的絕對值需恰好為 1。"""
        self.assertEqual(std.solve("2 3 4"), "Jolly")

    def test_length_two_not_jolly(self):
        """長度為 2：差的絕對值不為 1 → Not jolly。"""
        self.assertEqual(std.solve("2 1 5"), "Not jolly")

    def test_repeated_differences(self):
        """相鄰差重複（集合大小 < n-1）→ Not jolly。"""
        # 1 2 3 4：差全為 1，集合={1} ≠ {1,2,3}
        self.assertEqual(std.solve("4 1 2 3 4"), "Not jolly")

    def test_negative_numbers(self):
        """含負數的序列只要差值集合正確就是 Jolly。"""
        # -1 0 2：abs(-1-0)=1, abs(0-2)=2 → {1,2} = {1,2} → Jolly
        self.assertEqual(std.solve("3 -1 0 2"), "Jolly")

    def test_multiple_lines(self):
        """多行輸入，每行獨立判斷。"""
        text = "4 1 4 2 3\n5 1 4 2 -1 6\n1 100\n"
        expected = "Jolly\nNot jolly\nJolly"
        self.assertEqual(std.solve(text), expected)

    def test_easy_matches_standard(self):
        """easy 版與標準版輸出需完全一致。"""
        text = "4 1 4 2 3\n5 1 4 2 -1 6\n2 10 11\n"
        self.assertEqual(std.solve(text), easy.solve(text))

    def test_hand_matches_standard(self):
        """hand（手打）版輸出需與標準版完全一致。"""
        text = "4 1 4 2 3\n5 1 4 2 -1 6\n2 10 11\n"
        self.assertEqual(std.solve(text), hand.solve(text))


if __name__ == "__main__":
    unittest.main(verbosity=2)
