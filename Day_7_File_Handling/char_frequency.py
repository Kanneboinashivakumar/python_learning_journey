frequency = {}
with open("sample.txt", "r") as file:
    text = file.read()
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

for ch, count in frequency.items():
    print(repr(ch), ":", count)