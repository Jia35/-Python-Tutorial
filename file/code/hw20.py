while True:
    num = input("輸入:")

    if num[-1]=='C':
        out = int(num[:-1])*(9/5)+32
        print(out,'F')
    else:
        out = (int(num[:-1])-32)*5/9
        print(out,'C')

    print()
