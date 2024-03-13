#write program for built in function 


# print('''Built in functions like "min" "max" "type" "range" "print" "slice" "power" ''')
# list =( '1','2' , '3', '4', '5', '6')
# print(list[slice(3)])
# print(min(list))
# print(max(list))
# print(type(list))
# print(bool(1))

# for num in range (1,11):
#     print(num)   

#User defined function 
    
num = int(input("Enter the num of which you want table: \n")) 
   
def table(num):
    for i in range(1,11):
        result=num*i
        print(num ,  "X" , i , "=" , result)
table(num)
    
        

 



