# Week 02 作業說明（1114405041）

## 1. 完成題目清單
- Task 1：`task1_sequence_clean.py`
- Task 2：`task2_student_ranking.py`
- Task 3：`task3_log_summary.py`

## 2. 執行方式
- Python 版本：3.14.3

### 程式執行指令
```bash
python task1_sequence_clean.py
python task2_student_ranking.py
python task3_log_summary.py
```

### 測試執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 3. 各題資料結構選擇理由
- Task 1：使用 `list` 保留輸入順序，`set` 僅用來記錄是否看過，達成「去重但保序」。
- Task 2：使用 `list[tuple]` 搭配 `sorted(key=...)` 一次完成多層排序規則。
- Task 3：使用 `defaultdict(int)` 統計 user 次數，`Counter` 統計 action 次數，語意清楚且程式簡潔。

## 4. 遇到的錯誤與修正
- 錯誤：Task 3 在 `m=0` 時原本沒有輸出 top action，導致邊界測試失敗。
- 修正：在 `summarize()` 補上空輸入分支，回傳 `("None", 0)` 對應輸出 `top_action: None 0`。

## 5. Red → Green → Refactor 摘要

### Task 1
- Red：先寫 `test_sample_output`、`test_empty_input`，當時核心函式尚未實作，測試失敗。
- Green：先補 `parse_numbers`、`dedupe_keep_order` 與 `solve` 最小可行版本，使三個測試通過。
- Refactor：將輸出組裝抽成 `format_line`，統一空列表與一般列表輸出格式。

### Task 2
- Red：先寫範例排序與 tie-break 測試，尚未有 `rank_students`，測試失敗。
- Green：補齊 `parse_input`、`rank_students`，用 `sorted(key=lambda s: (-score, age, name))` 讓測試轉綠。
- Refactor：把解析與排序分成獨立函式，`solve` 只負責流程整合與輸出。

### Task 3
- Red：先寫 `test_sample_output` 與 `test_empty_logs`，空輸入情境不符合預期。
- Green：加入 `defaultdict` + `Counter` 統計邏輯，並補空輸入輸出規則。
- Refactor：把統計拆成 `summarize()`，讓排序規則（次數降冪、名稱升冪）集中管理。
