# 函式(有回傳值)
def add(x, y):
    sum = (x + y) * 1.03
    return sum

# 函式(無回傳值)
def addAndPrint(x, y):
    sum = (x + y) * 1.03
    print(sum)
    return 

print(((1 + 2) * 1.03))
print(((2 + 5) * 1.03))
print(add(1, 2))
print(add(2, 5))
addAndPrint(1, 2)
addAndPrint(2, 5)

