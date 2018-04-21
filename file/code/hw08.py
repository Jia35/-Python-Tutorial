x = input('運算符號: ')
a = int(input('整數1: '))
b = int(input('整數2: '))

if x == '+':
    print('結果= ', a+b)
elif x == '-':
    print('結果= ', a-b)
elif x == '*':
    print('結果= ', a*b)
elif x == '/':
    print('結果= ', a/b)
else:
    print('錯誤')
