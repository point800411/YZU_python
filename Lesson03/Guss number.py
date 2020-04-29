import random as r
while True:
    max = int(input('請輸入最大範圍:'))
    min = int(input('請輸入最小範圍:'))
    if max > min:
        break
    else:
        print('請輸入正確範圍')
        continue

n = r.randint(min, max)
while True:
    a = int(input('猜數字(%d - %d):' % (min, max)))
    if a > max or a < min:
        print('請輸入範圍數字')
        continue
    if a == n:
        print('答對了')
        break;
    elif a > n:
        max = a
    else:
        min = a

