#!/usr/bin/python3
# Palindrome Check Function on Python 3

# The Palindrome Algorithm
# this takes in a string and returns a boolean equal to the result of
# whether the program is a palindrome or not.
def palindrome(s: str) -> bool:
    # Reverse string using idiomatic python
    reversed_string = s[::-1]
    # return the answer, by comparing string and its reverse
    return s == reversed_string


# A utility function to output the result of palindromes
def is_palindrome(s: str):
    # if string is palindrome
    if palindrome(s):
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")


# main program
if __name__ == "__main__":
    string_1 = "abba"
    string_2 = "abbcccbba"
    string_3 = "abbccbbba"
    is_palindrome(string_1)
    is_palindrome(string_2)
    is_palindrome(string_3)
