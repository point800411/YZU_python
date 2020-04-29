import random as r
poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
# 計算分數
def GetScore(po): # 假設 po = ['A', 9, 'J']
    sum = 0
    for p in po:
        if p == 'A':
            sum = sum + 1
            continue
        if p == 'J' or p == 'Q' or p == 'K':
            sum = sum + 0.5
            continue
        sum = sum + p
    return sum
# 是否要補牌
