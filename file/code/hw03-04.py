print('A+B')
A = input('請輸入A:')
B = input('請輸入B:')
A = int(A)
B = int(B)
print('等於:',A+B)

print('-'*10)

if A+B >= 100:
    print('總和大於等於100')
elif A+B >= 10:
    print('總和大於等於10')
else:
    print('總和小於10')
