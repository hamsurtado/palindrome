
# function that tells you if string can be made into palindrome, 
# case insensitive, 
# returns True if empty string

def check_palindrome(str):
    char_count = {}
    for char in str.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    odd_count = 0
    for char in char_count:
        if char_count[char] % 2 != 0:
            odd_count += 1

            if odd_count > 1:
                return False
    
    return True
