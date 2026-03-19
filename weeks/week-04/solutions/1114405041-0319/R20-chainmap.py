# R20. ChainMap 合併映射（1.20）

"""
重點說明：
ChainMap 把多個字典「串成一條鏈」，查找鍵值時會依序搜尋每個字典，
找到第一個就回傳（不會繼續往後找）。
特性：
  - 查找（read）：依序從第一個字典開始找，最先找到的勝出。
  - 寫入（write）：一律只寫入「第一個」字典，其他字典不受影響。
  - 底層仍是原本的字典物件，修改會反映回去（非複製）。
  - 常見用途：設定檔優先順序（命令列 > 環境變數 > 預設值）。
"""

from collections import ChainMap

# ── 範例一：基本查找（優先取用第一個字典的值） ──────────────────
a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}   # 'z' 在 a 和 b 都有，a 優先
c = ChainMap(a, b)

print("=== 基本查找 ===")
print("a =", a)
print("b =", b)
print("c['x'] =", c["x"])   # 只在 a 裡，取到 1
print("c['y'] =", c["y"])   # 只在 b 裡，取到 2
print("c['z'] =", c["z"])   # a 和 b 都有，取 a 的 3（第一個字典優先）

# 可用 .keys() 看到所有字典合併後的鍵（重複鍵只出現一次）。
print("所有鍵：", list(c.keys()))
print("所有值：", list(c.values()))   # 同鍵只取第一個字典的值

# ── 範例二：寫入只影響第一個字典 ──────────────────────────────
c["x"] = 100    # 寫入 a 的 'x'
c["w"] = 999    # 'w' 不存在，新增到 a

print("\n=== 寫入後 ===")
print("c['x'] =", c["x"])
print("a（被修改）:", a)    # 'w' 和 'x' 都在 a 裡
print("b（未修改）:", b)    # b 不受影響

# ── 範例三：設定檔優先順序（常見實際應用） ──────────────────────
# 命令列引數 > 環境變數 > 預設值，越靠前優先級越高。
cli_args  = {"debug": True, "port": 8080}
env_vars  = {"port": 5000, "host": "localhost"}
defaults  = {"debug": False, "port": 3000, "host": "0.0.0.0"}

config = ChainMap(cli_args, env_vars, defaults)
print("\n=== 設定檔優先順序 ===")
print("debug :", config["debug"])   # 取 cli_args 的 True
print("port  :", config["port"])    # 取 cli_args 的 8080
print("host  :", config["host"])    # cli_args 沒有，取 env_vars 的 localhost

# ── 補充：new_child() 建立「子層」，不汙染原有鏈 ──────────────
# new_child() 會在鏈的最前面插入一個全新空字典，
# 適合在函式/迴圈內做「區域覆寫」而不影響外層設定。
local_config = config.new_child({"port": 9999})
print("\n=== new_child ===")
print("區域 port：", local_config["port"])   # 9999
print("原始 port：", config["port"])          # 8080（未被影響）

