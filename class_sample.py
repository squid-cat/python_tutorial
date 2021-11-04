# クラスの宣言 (Dentaku っていう型を作るよ！)
class Dentaku():

    # 初期化するメソッド(クラスを作成した時に自動的に発火するよ！)
    def __init__(self):
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.operation = '+'


    # 足し算か引き算かを判別 => 計算するメソッド
    def do_operation(self):
        if self.operation == '+':
            self.result = self.first_term + self.second_term
        elif self.operation == '-':
            self.result = self.first_term - self.second_term
        

# 変数:dentaku に クラス(型):Dentaku を作成するよ！(インスタンス化)
dentaku = Dentaku()


# 無限ループだ！！
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