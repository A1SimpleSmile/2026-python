"""UVA 948 - 單元測試

測試假幣識別邏輯，涵蓋：
- 能確定較輕假幣的情況
- 能確定較重假幣的情況
- 天平平衡排除法（未參與即為假幣）
- 無法唯一確定時輸出 0
- 多組測資格式（結果間空行）
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


std  = _load("uva948.py")
easy = _load("uva948-easy.py")
hand = _load("uva948-hand.py")


class TestUVA948(unittest.TestCase):

    def test_lighter_coin_identified(self):
        """兩次秤重都顯示 1 號在輕側 → 1 是較輕假幣。

        格式：1 組測資，N=3, K=2
        秤重1：Pi=1，左[1] vs 右[2]，結果 <
        秤重2：Pi=1，左[1] vs 右[3]，結果 <
        """
        inp = "1\n\n3 2\n1 1 2\n<\n1 1 3\n<"
        self.assertEqual(std.solve(inp), "1")

    def test_equal_weighing_excludes_participants(self):
        """天平平衡代表 1 和 2 都是真幣，未參與的 3 號是假幣。

        格式：N=3, K=1
        秤重：Pi=1，左[1] vs 右[2]，結果 =
        """
        inp = "1\n\n3 1\n1 1 2\n="
        self.assertEqual(std.solve(inp), "3")

    def test_ambiguous_returns_zero(self):
        """只有一次不平衡秤重，1 或 2 都有可能是假幣 → 輸出 0。

        格式：N=3, K=1
        秤重：Pi=1，左[1] vs 右[2]，結果 <（1 可能輕或 2 可能重）
        """
        inp = "1\n\n3 1\n1 1 2\n<"
        self.assertEqual(std.solve(inp), "0")

    def test_heavier_coin_identified(self):
        """兩次秤重都顯示 1 號在重側 → 1 是較重假幣。

        格式：N=3, K=2，結果都是 >（左重）
        """
        inp = "1\n\n3 2\n1 1 2\n>\n1 1 3\n>"
        self.assertEqual(std.solve(inp), "1")

    def test_multiple_cases_separated_by_blank_line(self):
        """多組測資各自輸出正確結果，且以空行分隔。"""
        inp = "2\n\n3 2\n1 1 2\n<\n1 1 3\n<\n\n3 1\n1 1 2\n="
        self.assertEqual(std.solve(inp), "1\n\n3")

    def test_easy_matches_standard(self):
        """easy 版與標準版輸出需完全一致。"""
        inp = "2\n\n3 2\n1 1 2\n<\n1 1 3\n<\n\n3 1\n1 1 2\n="
        self.assertEqual(std.solve(inp), easy.solve(inp))

    def test_hand_matches_standard(self):
        """hand（手打）版輸出需與標準版完全一致。"""
        inp = "2\n\n3 2\n1 1 2\n<\n1 1 3\n<\n\n3 1\n1 1 2\n="
        self.assertEqual(std.solve(inp), hand.solve(inp))


if __name__ == "__main__":
    unittest.main(verbosity=2)
