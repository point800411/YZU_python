# x1, y1 = 10, 20
# x2, y2 = 30, 40
# d=?
import math

x1 = int(input('請輸入x1='))
y1 = int(input('請輸入y1='))
x2 = int(input('請輸入x2='))
y2 = int(input('請輸入y2='))
d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
print("%.1f" %d)