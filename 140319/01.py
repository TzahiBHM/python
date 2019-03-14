"""
age=input("Enter You Age") #the input will be string
print(age*3) #result for 2: 222
age=int(age) #parse string to int
print(age*3) #result for 2: 6
"""
age = input("Enter Your Age: ")
age=int(age)
if age<0:
    print("Invalid Age")
elif age<18:
    print("To young")
    print("Your age is",age)
else:
    print("To Old")