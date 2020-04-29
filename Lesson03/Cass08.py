text = "半徑=10"

name, r = text.split("=")
r = int(r)
print("%s 為 %d 的面積是 %.2f" % (name, r, r * r * 3.14))