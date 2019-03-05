maxlevel=5
num=1
for num in range(maxlevel+1):
    for i in range(maxlevel-num+1):
        print(' ',end='')
    for i in range(2*num-1):
        print('*',end='')
    print()