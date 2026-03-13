# TEST_LOG.md

## Run 1 - Red
- 執行指令：
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
- 測試總數：9
- 通過數：0
- 失敗數：9（初版尚未實作 `task1/2/3` 核心函式）
- 從失敗到通過的修改：完成三個 task 檔案主流程與函式，並修正 Task 3 的空輸入行為。

## Run 2 - Green
- 執行指令：
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
- 測試總數：9
- 通過數：9
- 失敗數：0
- 摘要：
```text
Ran 9 tests in 0.001s
OK
```
- 從失敗到通過的修改：
	1. Task 1 補 `dedupe_keep_order()` 與空輸入輸出格式。
	2. Task 2 補 `sorted(..., key=...)` 多條件排序規則。
	3. Task 3 補 `defaultdict + Counter` 統計與 `m=0` 邊界處理。
