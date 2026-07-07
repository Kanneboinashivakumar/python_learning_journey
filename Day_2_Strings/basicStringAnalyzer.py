text = input("Enter a string: ")

if len(text) == 0:
    print("Empty string")
else:
    print("Length:", len(text))
    print("First character:", text[0])
    print("Last character:", text[-1])
    print("Reversed:", text[::-1])