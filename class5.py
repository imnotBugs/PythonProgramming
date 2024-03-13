# #Write code reading the flowchart and algorithm
# HOURS = float(input("Enter Hour: \n"))
# PAYTYPE = input("Enter Paytype: \n")
# RATE = float(input("Enter Rate: \n"))
# SALARY = float(input("Enter Salary: \n"))
# if PAYTYPE == "HOURLY":
#     if HOURS > 40:
#         pay = RATE *((40 +1.5)* (HOURS - 40))
#     else:
#         pay = RATE* HOURS
# else:
#     pay = SALARY
    
# print ("Pay for the employee is $",pay)

# Write a Python program to check whether the inputed no. is palindrome or not-----------------------------------------------------------
# def is_palindrome(num):
#     num = str(num)
#     return num == num[::-1]

# number = int(input('Enter a number: '))
# if is_palindrome(number):
#     print('The given number is Palindrome')
# else:
#     print('The given number is Not Palindrome')

#Another way of writing using while loop 
    # num = int(input("Enter a Number : \n"))
    # temp = num
    # reverse  = 0 
    # while(temp>0):
    #     last_digit = temp % 10
    #     reverse = (reverse * 10 ) + last_digit
    #     temp = temp // 10

    # if num  == reverse:
    #     print("Given No. is Palindrome")
    # else:
    #     print("Not Palindrome")

#Fibbonaci series

# n = 10

# first_term = 0 
# second_term = 1

# print(first_term , second_term, end = " ")
# for i in range(2, n):
#     next_term = first_term + second_term
#     print(next_term, end= " ")
#     first_term = second_term
#     second_term = next_term 



    
