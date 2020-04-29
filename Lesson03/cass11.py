n = int(input('請輸入數字'))
check = True
for i in range(1, n+1):
    if n % i == 0:
        print(i)

        