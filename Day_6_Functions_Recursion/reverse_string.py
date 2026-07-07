def reverse(text):
    if text == "":
        return ""
    return reverse(text[1:]) + text[0]

word = input("Enter a string: ")

print(f"Reversed string: {reverse(word)}")