My_age=26
Guess_age=0
print ("Please guess how old I am!!!")
input(Guess_age)
while Guess_age!=My_age:
    if Guess_age < My_age:
        print("so young!!!")
        input(Guess_age)
    else :
        print("so old!!!")
        input(Guess_age)
print("wonderful!!!")
