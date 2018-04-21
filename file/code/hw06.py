num = int(input('請輸入一個數:'))
x = 0
num_all = 0

while num_all <= num:
    x += 1
    num_all += x
    print(x)
    print(num_all)
    print('-----')

print('當數值到',x,'時,總和會超過',num)
