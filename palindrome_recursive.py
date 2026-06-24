def palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return palindrome(text[1:-1])

word = input("Enter a word: ").lower()
if palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")