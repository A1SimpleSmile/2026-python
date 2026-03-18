"""UVA 10008 - 單元測試

測試字母頻率統計與排序是否符合題目規則：
- 大小寫視同（a == A）
- 依次數由大到小排列
- 次數相同時按字母 A→Z 排列
- 未出現的字母不輸出
"""

import unittest
import importlib.util
import pathlib

BASE = pathlib.Path(__file__).parent


def _load(filename: str):
    """以絕對路徑載入 Python 模組，支援檔名含 - 的情況。"""
    name = filename.replace(".py", "").replace("-", "_")  # 轉成合法模組名稱
    spec = importlib.util.spec_from_file_location(name, BASE / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


std  = _load("uva10008.py")
easy = _load("uva10008-easy.py")
hand = _load("uva10008-hand.py")


class TestUVA10008(unittest.TestCase):

    def test_output_format(self):
        """每行輸出格式應為「大寫字母 空格 正整數」。"""
        text = "1\nHello World\n"
        out = std.solve(text)
        for line in out.splitlines():
            parts = line.split()
            self.assertEqual(len(parts), 2, msg=f"格式錯誤: {line!r}")
            self.assertTrue(parts[0].isupper() and len(parts[0]) == 1)
            self.assertGreater(int(parts[1]), 0)

    def test_sorted_descending_by_count(self):
        """輸出必須依出現次數由大到小排列。"""
        text = "1\naabbbbcc\n"  # B:4, A:2, C:2
        out = std.solve(text)
        counts = [int(line.split()[1]) for line in out.splitlines()]
        self.assertEqual(counts, sorted(counts, reverse=True))

    def test_same_count_alphabetical(self):
        """次數相同時按字母 A→Z 順序排列。"""
        text = "1\nabc\n"       # A:1, B:1, C:1 → 應輸出 A B C 順序
        out = std.solve(text)
        chars = [line.split()[0] for line in out.splitlines()]
        self.assertEqual(chars, sorted(chars))

    def test_case_insensitive(self):
        """大寫與小寫視為同一字母。"""
        text = "1\nAaAa\n"      # A 出現 4 次
        self.assertEqual(std.solve(text).strip(), "A 4")

    def test_skip_non_alpha(self):
        """數字、符號、空白不計入。"""
        text = "1\n123 !@# abc\n"   # 只有 A:1, B:1, C:1
        lines = std.solve(text).splitlines()
        self.assertEqual(len(lines), 3)

    def test_only_specified_lines_counted(self):
        """只統計前 n 行，多餘的行不計。"""
        # n=1，只分析 "aaa"，第二行 "bbb" 不應被計入
        text = "1\naaa\nbbb\n"
        out = std.solve(text)
        self.assertNotIn("B", out)
        self.assertIn("A 3", out)

    def test_easy_matches_standard(self):
        """easy 版輸出需與標準版完全一致。"""
        text = "2\nHello World\nPython Programming\n"
        self.assertEqual(std.solve(text), easy.solve(text))

    def test_hand_matches_standard(self):
        """hand（手打）版輸出需與標準版完全一致。"""
        text = "2\nHello World\nPython Programming\n"
        self.assertEqual(std.solve(text), hand.solve(text))


if __name__ == "__main__":
    unittest.main(verbosity=2)
