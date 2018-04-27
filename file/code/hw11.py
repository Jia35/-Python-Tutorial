x = []

while True :
    a = int(input('輸入數字:'))
    if a==0:
        break
    x.append(a)

x.sort()
print('排序後-->',x)
