# 數組 List(可重複), Set(不可重複), Dict(Key-Volue)
scores = [100, 90, 80]
scores.append(70)
print(scores)  # 列印數組
print(scores[0])  # 取的維度=0的內容
print(len(scores))  # 取得數組長度(有幾筆資料)
print(scores.index(100))  # 取得內容=100的內容

for x in scores:
    print(scores.index(x), x)

for (i, x) in enumerate(scores):
    print(i, x)
