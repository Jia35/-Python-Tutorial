d = int(input("幾位數?"))

for i in range(0, 10**d):
    num = str(i).zfill(d)
    num1 = int(num[:d//2])
    num2 = int(num[d//2:])
    
    if (num1+num2)**2 == int(num):
        print(num)
