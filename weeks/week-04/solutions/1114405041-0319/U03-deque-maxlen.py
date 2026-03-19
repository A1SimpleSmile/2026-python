# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）

"""
重點說明：
  deque(maxlen=N) 是一個「固定容量」的雙端佇列（double-ended queue）。
  當佇列已滿再 append 時，Python 會「自動從另一端移除最舊的元素」，
  不需要手動刪除，因此永遠只保留最近 N 筆資料。
  常見應用：保留最近 N 行日誌、滑動視窗計算、歷史記錄限制。
"""

from collections import deque

# ── 示範一：逐步 append，觀察自動淘汰行為 ───────────────────────────
q = deque(maxlen=3)
print("=== 逐步 append（maxlen=3）===")
for i in [1, 2, 3, 4, 5]:
    q.append(i)
    print(f"append({i}) → {list(q)}")
    # 說明：當 deque 滿了（長度 = 3），再 append 就自動從左端（最舊）踢掉一個元素。

print(f"最終結果：{list(q)}")   # [3, 4, 5]

# ── 示範二：appendleft 從左端加入，自動淘汰右端（最舊） ─────────────
q2 = deque(maxlen=3)
print("\n=== appendleft（maxlen=3）===")
for i in [1, 2, 3, 4, 5]:
    q2.appendleft(i)
    print(f"appendleft({i}) → {list(q2)}")

# ── 示範三：沒有 maxlen 的 deque 可無限成長 ──────────────────────────
q_unlim = deque()
q_unlim.extend([10, 20, 30])
print("\n=== 沒有 maxlen ===")
print(f"deque 長度：{len(q_unlim)}，內容：{list(q_unlim)}")

# ── 示範四：實際應用：保留最後 3 行 log ──────────────────────────────
log_buffer = deque(maxlen=3)
logs = [
    "[INFO] 服務啟動",
    "[INFO] 接收到請求",
    "[WARNING] 回應時間過長",
    "[ERROR] 資料庫連線失敗",
    "[INFO] 重試連線成功",
]
for line in logs:
    log_buffer.append(line)

print("\n=== 最後 3 行 log ===")
for line in log_buffer:
    print(" ", line)

