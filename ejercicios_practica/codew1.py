"""
Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.

"""

def reverse_words(text):
    words = text.split(" ")
    reversed_words = []
    for i in words:
        reversed_words.append(i[::-1])
    return " ".join(reversed_words)

"""
Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.
"""

def repeat_str(repeat, string):
    new_string = []
    for i in range(repeat):
        new_string.append(string)
    return "".join(new_string)

# Otra opcion
def repeat_str(repeat, string):
    return string * repeat

"""
Write a function that takes an array of numbers and returns the sum of the numbers. 
The numbers can be negative or non-integer. 
If the array does not contain any numbers then you should return 0.

"""

def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum

