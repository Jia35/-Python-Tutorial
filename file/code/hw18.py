a = input("請輸入:")
print(a.upper())

f = open('test.txt', 'a')
f.write(a.upper())
f.close()
