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