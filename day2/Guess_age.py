8：猜年龄游戏升级版
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