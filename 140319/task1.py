number = int(input("Enter number: "))
if number>0 and number <10: #if one digit
    if number==1:
        print("One")
    elif number==2:
        print("Two")
    elif number==3:
        print("Three")
    elif number==4:
        print("Four")
    elif number==5:
        print("Five")
    elif number ==6:
        print("Six")
    elif number==7:
        print("Seven")
    elif number==8:
        print("eight")
    elif number==9:
        print("Nine")
elif number>9 and number <100: #if 2 digits
    x=number//10
    y=number%10
    print(x+y)
elif number>99 and number<1000: #if 3 digits
    #145
    x=number //100 # 1
    y = (number//10) % 10 # 4
    z = number %10 # 5  
    print(x*y*z)
else:
    print("above 3 digits")