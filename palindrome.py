def ispalindrome(s):
    return s == s[::-1]
s = str(input("Enter the word: "))
if ispalindrome(s):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")