# Write python program to print list of numbers using range and for loop
print("----------------------------Question: 1---------------------------------------------")
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(numList)
for num in range(n):
    print(numList[num])


# Write python program to print first n prime numbers without using function
print("----------------------------Question: 2---------------------------------------------")
n = 10 # kitne prime number chahiye
count = 0
num = 2

while count < n: 
    is_prime = True

    for i in range(2, num): 
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        count += 1

    num += 1

print()

# write python program to multiply two matrices
print("----------------------------Question: 3---------------------------------------------")
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows of matrix1
for i in range(len(matrix1)):
    # iterate through columns of matrix2
    for j in range(len(matrix2[0])):
        # iterate through rows of matrix2
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for row in result:
    print(row)



# Write python program to take command line arguments (word count)
print("----------------------------Question: 4---------------------------------------------")
import sys
number_of_arguments = len(sys.argv)
word_count = 0
for i in range(1, number_of_arguments):
    print(sys.argv[i])
    word_count += 1
print("Word count:",word_count)