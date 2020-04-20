w = int(input('請輸入體重:'))
h = int(input('請輸入升高:'))
BMI = w / (h/100) ** 2

if BMI > 23 :
    R = "過胖"
elif BIM < 18 :
    R = "過瘦"
else:
    R = "正常"
print(w, h, BMI, R)
print("身高: %.1f 體重: %.1f BMI= %.2f Result= %s"%
      (w, h, BMI, R))