def mask(money) :
    x = money // 5
    size = "成人"
    return x, size

my_x, my_size = mask(100) #回傳的名稱不用語函式一樣
print(my_x, my_size)
