"""UVA 10035 - 單元測試

測試直式加法進位次數計算，重點驗證：
- 零次進位輸出「No carry operation.」
- 一次進位輸出「1 carry operation.」（無 s）
- 多次進位輸出「n carry operations.」（有 s）
- 終止條件「0 0」正確處理
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


std  = _load("uva10035.py")
easy = _load("uva10035-easy.py")
hand = _load("uva10035-hand.py")


class TestUVA10035(unittest.TestCase):

    def test_no_carry(self):
        """各位相加均不超過 9，輸出 'No carry operation.'"""
        # 123 + 456：3+6=9, 2+5=7, 1+4=5，無進位
        self.assertEqual(std.solve("123 456\n0 0"), "No carry operation.")

    def test_one_carry(self):
        """恰好一次進位，輸出 '1 carry operation.'（operation 無複數 s）。"""
        # 9 + 1 = 10：個位進位一次
        self.assertEqual(std.solve("9 1\n0 0"), "1 carry operation.")

    def test_multiple_carries(self):
        """多次進位，輸出複數 'carry operations'。"""
        # 555 + 555：個位 5+5=10（進位1），十位 5+5+1=11（進位2），百位 5+5+1=11（進位3）
        self.assertEqual(std.solve("555 555\n0 0"), "3 carry operations.")
        # 99 + 11：個位 9+1=10（進位1），十位 9+1+1=11（進位2）
        self.assertEqual(std.solve("99 11\n0 0"), "2 carry operations.")

    def test_sample_input(self):
        """題目的標準範例對應輸出。"""
        text = "123 456\n555 555\n123 594\n0 0\n"
        # 123+594：3+4=7（無），2+9=11（進位1），1+5+1=7（無）→ 1次
        expected = "No carry operation.\n3 carry operations.\n1 carry operation."
        self.assertEqual(std.solve(text), expected)

    def test_zero_operand(self):
        """其中一個運算元為 0，不應有進位。"""
        self.assertEqual(std.solve("0 999\n0 0"), "No carry operation.")

    def test_stop_at_double_zero(self):
        """遇到 '0 0' 後停止，之後的行不應被處理。"""
        text = "9 1\n0 0\n555 555\n"
        out = std.solve(text)
        self.assertEqual(out, "1 carry operation.")  # 第二組不應出現

    def test_easy_matches_standard(self):
        """easy 版與標準版輸出需完全一致。"""
        text = "9 9\n19 1\n5 5\n0 0\n"
        self.assertEqual(std.solve(text), easy.solve(text))

    def test_hand_matches_standard(self):
        """hand（手打）版輸出需與標準版完全一致。"""
        text = "9 9\n19 1\n5 5\n0 0\n"
        self.assertEqual(std.solve(text), hand.solve(text))


if __name__ == "__main__":
    unittest.main(verbosity=2)
