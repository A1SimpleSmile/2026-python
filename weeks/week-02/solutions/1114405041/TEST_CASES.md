# TEST_CASES.md - 測試案例設計

## Case 1：Task 1 一般情況（正常輸入）
- 輸入：`5 3 5 2 9 2 8 3 1`
- 預期輸出：
```text
dedupe: 5 3 2 9 8 1
asc: 1 2 2 3 3 5 5 8 9
desc: 9 8 5 5 3 3 2 2 1
evens: 2 2 8
```
- 實際輸出：同預期
- 是否通過：PASS
- 對應測試：`tests/test_task1.py::TestTask1SequenceClean.test_sample_output`
- 關鍵修改點：補齊 `dedupe_keep_order()`，不可用 set 直接輸出。

## Case 2：Task 1 邊界情況（空輸入）
- 輸入：空字串
- 預期輸出：
```text
dedupe:
asc:
desc:
evens:
```
- 實際輸出：同預期
- 是否通過：PASS
- 對應測試：`tests/test_task1.py::TestTask1SequenceClean.test_empty_input`
- 關鍵修改點：加入 `format_line()` 統一空列表輸出格式。

## Case 3：Task 2 同分排序情況
- 輸入（概念）：`("amy",88,19), ("bob",88,19), ("zoe",88,20)`
- 預期輸出順序：`amy -> bob -> zoe`
- 實際輸出順序：`amy -> bob -> zoe`
- 是否通過：PASS
- 對應測試：`tests/test_task2.py::TestTask2StudentRanking.test_tie_break_age_then_name`
- 關鍵修改點：改為單次 key 排序 `(-score, age, name)`。

## Case 4：Task 3 反例（容易寫錯）
- 輸入：
```text
4
bob login
amy view
bob logout
amy login
```
- 預期輸出：
```text
amy 2
bob 2
top_action: login 2
```
- 實際輸出：同預期
- 是否通過：PASS
- 對應測試：`tests/test_task3.py::TestTask3LogSummary.test_user_sort_tie_by_name`
- 關鍵修改點：使用者排序加上名稱次排序，避免同次數順序不穩定。

## Case 5：Task 3 最能測出錯誤的一組（空輸入）
- 輸入：
```text
0
```
- 預期輸出：
```text
top_action: None 0
```
- 實際輸出：同預期
- 是否通過：PASS
- 對應測試：`tests/test_task3.py::TestTask3LogSummary.test_empty_logs`
- 關鍵修改點：`summarize()` 補上空 logs 分支。