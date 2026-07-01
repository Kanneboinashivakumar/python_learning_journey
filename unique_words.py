with open("sample.txt", "r") as file:
    text = file.read().lower()
words = text.split()
unique = sorted(set(words))
print("Unique Words:")
for word in unique:
    print(word)