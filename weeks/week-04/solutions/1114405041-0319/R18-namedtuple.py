# R18. namedtuple（1.18）

"""
重點說明：
namedtuple 是 tuple 的子類別，每個欄位都有名稱，
讓程式碼比普通 tuple（只能用 s[0]、s[1]）更易讀。
特性：
  - 不可變（immutable），和一般 tuple 相同。
  - 可用「屬性名稱」存取欄位：s.name，也可用索引：s[0]。
  - 比建立完整 class 更輕量，適合用來當作純資料容器。
  - 用 _replace(**kwargs) 可以「複製並部分修改」，原物件不受影響。
"""

from collections import namedtuple

# ── 範例一：訂閱者 ──────────────────────────────────────
# 用 namedtuple 定義兩個欄位的「訂閱者」資料型別。
# 第一個參數是型別名稱（字串），第二個參數是欄位列表。
Subscriber = namedtuple("Subscriber", ["addr", "joined"])

sub = Subscriber("jonesy@example.com", "2012-10-19")

print("=== Subscriber ===")
print("完整物件：    ", sub)              # 印出時有欄位名稱，比 tuple 易讀
print("電子郵件：    ", sub.addr)         # 用屬性名稱存取
print("加入日期：    ", sub.joined)
print("用索引存取：  ", sub[0], sub[1])   # 同樣支援索引
print("是否為 tuple：", isinstance(sub, tuple))  # True，namedtuple 繼承自 tuple

# ── 範例二：股票 ──────────────────────────────────────────
# 新增 price 欄位，並示範計算屬性（total）。
Stock = namedtuple("Stock", ["name", "shares", "price"])

s = Stock("ACME", 100, 123.45)
print("\n=== Stock ===")
print("原始股票：    ", s)
print("名稱：        ", s.name)
print("股數：        ", s.shares)
print("單價：        ", s.price)
print("總市值：      ", s.shares * s.price)   # 自行組合欄位做計算

# _replace 回傳一個「新物件」，原本的 s 不受影響（不可變特性）。
# 常見用途：更新某個欄位的值，但保留其他欄位不變。
s_updated = s._replace(shares=75)
print("\n賣掉部分持股後（_replace）：", s_updated)
print("原物件未被修改：             ", s)

# ── 補充：_fields 屬性 ─────────────────────────────────
# _fields 可以拿到所有欄位名稱的 tuple，方便動態操作。
print("\nStock 的欄位名稱：", Stock._fields)

# 也可以把普通 dict 解包成 namedtuple，方便資料轉換。
raw = {"name": "AAPL", "shares": 50, "price": 612.78}
apple = Stock(**raw)
print("從 dict 建立的 Stock：", apple)

