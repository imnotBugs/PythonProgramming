#Write a computer program on the grading system of VIT
percentage =float(input("Enter Your percentage \n"))
if(percentage >= 90):
    print("Your Grade is S")
elif (percentage>=80):
    print("Your Grade is A")
elif (percentage>=70):
    print("Your Grade is B")
elif (percentage>=60):
    print("Your Grade is C")
elif (percentage>=50):
    print("Your Grade is D")
elif (percentage<40):
    print("You are a failure")

#Write a program to calculate greatest of three integers using nested if else
    num1=int(input("Enter First Number: "))
    num2=int(input("Enter Second Number: "))
    num3=int(input("Enter Third Number: "))
    
    if(num1 >= num2):
        if(num1 > num3):
            print(num1 + "is Greatest")
        else:
            print(num3 +" is Greatest")
    else: 
        if num3 >= num2:
            print(num3 +" is Greatest")
        else: 
            print(num2 + " Greatest")

#Draw the pattern given  below. without using any kind of loops
            '''1
               1  2
               1  2  3   '''
n = 5
if n>=1:
    print("1")
    if n>=2:
        print("1 2")
    if n>=3:
        print("1 2 3")
    if n>=4:
        print("1 2 3 4")






    
        
    

