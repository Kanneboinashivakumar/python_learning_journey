text = input("Enter a string: ")
text=text.lower()
if text == text[::-1]:
    print("Palindrome ")
else:
    print("Not a Palindrome ")