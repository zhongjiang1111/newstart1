#1. 使用while循环输出1 2 3 4 5 6     8 9 10
#2. 求1-100的所有数的和
#3. 输出 1-100 内的所有奇数
#4. 输出 1-100 内的所有偶数
#5. 求1-2+3-4+5 ... 99的所有数的和
#6. 用户登陆（三次机会重试）
#7：猜年龄游戏
#要求：
#    允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
#8：猜年龄游戏升级版
#要求：
#   允许用户最多尝试3次
#    每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，
#    如果回答N或n，就退出程序
#   如何猜对了，就直接退出

count=0
while count <= 10:
    print(count)
    count+=1
a=0
count=1
while count<=100:
    a+=count
    count += 1
    if count==101:
        print(a)

a=0
count=1
while count<=100:
    if count%2==1:
        a += count

    if count==100:
        print(a)
    count += 1

a=0
count=1
while count<=100:
    if count%2==0:
        a += count

    if count==100:
        print(a)
    count += 1
a=0
count=1
while count<=100:
    if count%2==0:
        a += count

    if count==100:
        print(a)
    count += 1