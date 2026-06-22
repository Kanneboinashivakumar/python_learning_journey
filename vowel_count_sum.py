text = input("Enter a string: ").lower()
count = (
    text.count("a") +
    text.count("e") +
    text.count("i") +
    text.count("o") +
    text.count("u")
)
print(f"No of vowels :{count}")