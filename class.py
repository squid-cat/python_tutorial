from typing import Awaitable


class StdInfo:

    def __init__(self, num, adr, p_num, adm, cry):
        self.number = num           # 学生番号: int
        self.address = adr          # 住所: str
        self.phone_number = p_num   # 電話番号: int
        self.admission_YM = adm     # 入学年月: str
        self.cry = cry              # 鳴き声: str

    # 電話番号を変更するメソッド
    def ChangePhoneNumber(self, phone_number):

        # 入力が整数型であるか
        if type(phone_number) == type(int()):
            self.phone_number = phone_number
            print('電話番号を変更しました')
        else:
            print('電話番号を変更しませんでした')


# インスタンス化
cat = StdInfo(123456, 'どこかの屋根', 222, '2020/4', 'にゃん')
bird = StdInfo(106331, 'どこかの森', 106, '2021/4', 'こけこっこ')


print(cat.number)
print(bird.number)
print(cat.address)
print(bird.address)


print(cat.phone_number)

# 電話番号の変更(整数型)
cat.ChangePhoneNumber(999)
print(cat.phone_number)

# 電話番号の変更(文字列)
cat.ChangePhoneNumber('これは文字列')
print(cat.phone_number)