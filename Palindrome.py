def palindrome(s):
    reversed_string = s[::-1]

    return s.replace(' ', '').lower() == reversed_string.replace(' ', '').lower()

print(palindrome("kayak"))

