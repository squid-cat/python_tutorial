# 関数を定義
def plus(a, b):
    result = a + b
    return result

print(plus(1, 2))       # 出力: 3
print(plus(5.3, -0.2))  # 出力: 5.1
print(plus(3, 5.5))     # 出力: 8.5



# グローバル変数
a = 0

# グローバル変数に引数:xを足す関数
def global_plus(x):
    # 関数内で「このグローバル変数を使うよー」と宣言する
    global a
    a = a + x

global_plus(3)
print(a)    # 出力: 3
global_plus(10)
print(a)    # 出力: 13
global_plus(-0.5)
print(a)    # 出力: 12.5