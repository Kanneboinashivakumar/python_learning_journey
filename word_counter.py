word_count = {}

with open("sample.txt", "r") as file:
    text = file.read().lower()

words = text.split()

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Total Words:", len(words))

print("\nWord Frequencies:")
for word, count in word_count.items():
    print(word, ":", count)