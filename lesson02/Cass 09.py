w = int(input('請輸入體重:'))
h = int(input('請輸入升高:'))
BMI = w / (h/100) ** 2

while BMI > 23 :
    R = "過胖"

print("身高: %.1f 體重: %.1 BMI= %.12f Result= %s")