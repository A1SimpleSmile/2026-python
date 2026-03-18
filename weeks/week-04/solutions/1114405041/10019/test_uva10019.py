"""UVA 10019 - 單元測試

測試 Hashmat 問題：輸出兩個整數差的絕對值。
重點測試：大數處理、順序不影響結果、多行輸入。
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


std  = _load("uva10019.py")
easy = _load("uva10019-easy.py")
hand = _load("uva10019-hand.py")


class TestUVA10019(unittest.TestCase):

    def test_basic_difference(self):
        """基本差值計算：小值在前。"""
        self.assertEqual(std.solve("10 20"), "10")

    def test_reversed_order(self):
        """大值在前也要輸出正整數（取絕對值）。"""
        self.assertEqual(std.solve("20 10"), "10")

    def test_equal_numbers(self):
        """兩數相等時差為 0。"""
        self.assertEqual(std.solve("5 5"), "0")

    def test_large_numbers(self):
        """題目說數字不超過 2^63，Python 可直接處理巨大整數。"""
        a = 2 ** 62 + 1
        b = 2 ** 62
        self.assertEqual(std.solve(f"{a} {b}"), "1")

    def test_very_large_difference(self):
        """超大差值（接近 2^63 量級）。"""
        self.assertEqual(std.solve(f"0 {2**63}"), str(2 ** 63))

    def test_multiple_lines(self):
        """處理多行輸入，每行各自獨立計算。"""
        text = "10 12\n5 12\n1 1\n"
        expected = "2\n7\n0"
        self.assertEqual(std.solve(text), expected)

    def test_easy_matches_standard(self):
        """easy 版與標準版輸出需完全一致。"""
        text = "100 200\n999 1000\n0 1000000\n"
        self.assertEqual(std.solve(text), easy.solve(text))

    def test_hand_matches_standard(self):
        """hand（手打）版輸出需與標準版完全一致。"""
        text = "100 200\n999 1000\n0 1000000\n"
        self.assertEqual(std.solve(text), hand.solve(text))


if __name__ == "__main__":
    unittest.main(verbosity=2)
