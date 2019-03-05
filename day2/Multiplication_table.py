for i in range(1,10):
    for j in range(1,i+1):
        print ('%s*%s=%s'%(i,j,i*j),end='')
    print()
#print默认是打印一行，结尾加换行。end=' '意思是末尾不换行，加空格。