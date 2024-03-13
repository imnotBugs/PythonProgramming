# Write a python function that prints out the first n rows of pascal's triangle
def print_pascals_triangle(n):
    for i in range(n):
        num = 1
        for k in range(n - i):
            print("", end=" ")
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()

print_pascals_triangle(5)

# write a python function to check whether a string is a pangram or not
def is_pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string.lower():
            return False
    return True

print(is_pangram("The quick brown fox jumps over the lazy dog"))

# write a python program that accepts a hyphen seperated sequence of words as input and prints the words in a hyphen seperated sequence after sorting them alphabetically
def sort_words(sequence):
    words = sequence.split("-")
    sorted_words = sorted(words)
    sorted_sequence = "-".join(sorted_words)
    return sorted_sequence

input_sequence = input("Enter a hyphen separated sequence of words: ")
sorted_sequence = sort_words(input_sequence)
print("Sorted sequence:", sorted_sequence)

# Write a python program to access a function inside a function
def outer_function():
    def inner_function():
        print("Inside inner function")
    
    print("Inside outer function")
    inner_function()

outer_function()

# Write a python program to detect the number of local variables declared in a function
def my_function():
    a = 1
    b = 2
    c = 3
    return a + b + c

print("Number of local variables:", len(my_function.__code__.co_varnames))

# Write a python program that invokes a function after a specified period of time
import time

def delayed_function():
    print("Delayed function called")

delay = 2

time.sleep(delay)
delayed_function()