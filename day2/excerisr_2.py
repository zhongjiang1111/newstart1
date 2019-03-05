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
#1. 使用while循环输出1 2 3 4 5 6     8 9 10

count=0
while count <= 10:
    print(count)
    count+=1
 # 2. 求1-100的所有数的和

a=0
count=1
while count<=100:
    a+=count
    count += 1
    if count==101:
        print(a)
 # 3. 输出 1-100 内的所有奇数
a=0
count=1
while count<=100:
    if count%2==1:
        a += count

    if count==100:
        print(a)
    count += 1
 # 4. 输出 1-100 内的所有偶数
a=0
count=1
while count<=100:
    if count%2==0:
        a += count

    if count==100:
        print(a)
    count += 1
# 5. 求1-2+3-4+5 ... 99的所有数的和
a=0
count=1
b=-1
while count<=100:
    c=b**(count-1)
    a += (count*c)
    if count==100:
        print(a)
    count += 1
#6. 用户登陆（三次机会重试）
name='zhongjiang'
password='123456'
num=1
while num<=3:
    in_name=input('用户名')
    in_password=input('password')
    if in_name==name and in_password==password:
        print('sign up wonderful')
        break
    else:
        print('输入错误 请重试')
    if num==3:
        print('你已经超过最大输出措数，已锁定')
    num += 1
#7：猜年龄游戏
#要求：
#    允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
age='18'
num=1
while num<=3:
    in_age=input('请输入年龄')
    if in_age==age:
        print('恭喜你猜对了')
        break
    else:
        print('fault')
    num+=1
#8：猜年龄游戏升级版
#要求：
#   允许用户最多尝试3次
#    每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，
#    如果回答N或n，就退出程序
#   如何猜对了，就直接退出
age='18'
tag=True
while tag:
    num = 1
    while num <= 3:
        in_age = input('请输入年龄')
        if in_age == age:
            print('恭喜你猜对了')
            break
        else:
            print('fault')
        num += 1
    if num<=3:
        break
    else:
        print('once agin?')
        guest=input('Y or N')
        if guest=='Y' or guest=='y' :
            tag=True
        else:
            tag=0
