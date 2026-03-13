# R14. 物件排序 attrgetter（1.14）

# attrgetter 和 itemgetter 類似，但目標是「物件屬性」。
from operator import attrgetter

class User:
    # 簡單使用者類別，只有 user_id 一個屬性。
    def __init__(self, user_id):
        self.user_id = user_id

# 一組物件資料。
users = [User(23), User(3), User(99)]

# 依 user_id 由小到大排序，回傳新的 list。
sorted(users, key=attrgetter('user_id'))
