# クラスの宣言 (Dentaku っていう型を作るよ！)
class Dentaku():

    # 初期化するメソッド(クラスを作成した時に自動的に発火するよ！)
    def __init__(self):
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.operation = '+'
        # 【補足】__init__(self)が発火したことを教える
        print("__init__(self)が発火したよ！")

    # 足し算か引き算かを判別 => 計算するメソッド
    def do_operation(self):
        if self.operation == '+':
            self.result = self.first_term + self.second_term
        elif self.operation == '-':
            self.result = self.first_term - self.second_term
        # 【補足】do_operation(self)が発火したことを教える
        print("do_operation(self)が発火したよ！")
        

# 変数:dentaku に クラス(型):Dentaku を作成するよ！
dentaku = Dentaku()

while True:
    # 入力(数字)
    f = int(input("First term "))
    # 入力結果を クラス内変数:first_term に格納
    dentaku.first_term = f

    # 入力(文字: + か -)
    o = input("Operation ")
    dentaku.operation=o

    # 入力(数字)
    s = int(input("Second term "))
    # 入力結果を クラス内変数:second_term に格納
    dentaku.second_term=s

    # メソッド:do_operation を発火
    dentaku.do_operation()

    # クラス内変数:result に格納されたものを出力
    r = dentaku.result
    print("Result ", r)