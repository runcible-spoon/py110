"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""

def palindrome_substrings(s):
    result = []
    substrings_list = substrings(s)

    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)

    return result

def is_palindrome(string):
    reversed_string = string[::-1]
    if reversed_string == string:
        return True
    else:
        return False

def substrings(string):
    result = []
    start_index = 0

    while start_index <= len(string) - 2:
        num_chars = 2
        while num_chars <= len(string) - start_index:
            substring = string[start_index:start_index + num_chars]
            result.append(substring)
            num_chars += 1
        
        start_index += 1

    return result

# Test cases:  

# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]
