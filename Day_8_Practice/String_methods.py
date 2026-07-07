# ==========================================
# PYTHON STRING METHODS
# ==========================================

s = "hello world"

# ------------------------------------------
# 1. upper() - Converts all letters to uppercase
# ------------------------------------------
print("upper():", s.upper())
# Output:
# upper(): HELLO WORLD

# ------------------------------------------
# 2. lower() - Converts all letters to lowercase
# ------------------------------------------
print("lower():", s.lower())
# Output:
# lower(): hello world

# ------------------------------------------
# 3. capitalize() - Capitalizes the first letter
# ------------------------------------------
print("capitalize():", s.capitalize())
# Output:
# capitalize(): Hello world

# ------------------------------------------
# 4. title() - Capitalizes the first letter of every word
# ------------------------------------------
print("title():", s.title())
# Output:
# title(): Hello World

# ------------------------------------------
# 5. swapcase() - Changes uppercase to lowercase and vice versa
# ------------------------------------------
print("swapcase():", s.swapcase())
# Output:
# swapcase(): HELLO WORLD

# ------------------------------------------
# 6. strip() - Removes spaces from both sides
# ------------------------------------------
s1 = "   Python   "
print("strip():",s1.strip())
# Output:
# strip():Python

# ------------------------------------------
# 7. lstrip() - Removes spaces from the left
# ------------------------------------------
print("lstrip():",s1.lstrip())
# Output:
# lstrip():Python

# ------------------------------------------
# 8. rstrip() - Removes spaces from the right
# ------------------------------------------
print("rstrip():",s1.rstrip())
# Output:
# rstrip():    Python

# ------------------------------------------
# 9. replace() - Replaces one substring with another
# ------------------------------------------
print("replace():", s.replace("world", "Python"))
# Output:
# replace(): hello Python

# ------------------------------------------
# 10. find() - Returns the first occurrence index(if not found -1)
# ------------------------------------------
print("find('o'):", s.find("o"))
# Output:
# find('o'): 4

# ------------------------------------------
# 11. index() - Returns index (Error if not found)
# ------------------------------------------
print("index('w'):", s.index("w"))
# Output:
# index('w'): 6

# ------------------------------------------
# 12. count() - Counts occurrences
# ------------------------------------------
print("count('l'):", s.count("l"))
# Output:
# count('l'): 3

# ------------------------------------------
# 13. startswith() - Checks starting characters
# ------------------------------------------
print("startswith('he'):", s.startswith("he"))
# Output:
# startswith('he'): True

# ------------------------------------------
# 14. endswith() - Checks ending characters
# ------------------------------------------
print("endswith('ld'):", s.endswith("ld"))
# Output:
# endswith('ld'): True

# ------------------------------------------
# 15. split() - Splits string into a list
# ------------------------------------------
numbers = "10 20 30"
print("split():", numbers.split())
# Output:
# split(): ['10', '20', '30']

# ------------------------------------------
# 16. join() - Joins list elements into a string
# ------------------------------------------
words = ["Python", "is", "easy"]
print("join():", " ".join(words))
# Output:
# join(): Python is easy

# ------------------------------------------
# 17. isalpha() - True if only alphabets
# ------------------------------------------
print("isalpha():", "Python".isalpha())
# Output:
# isalpha(): True

# ------------------------------------------
# 18. isdigit() - True if only digits
# ------------------------------------------
print("isdigit():", "12345".isdigit())
# Output:
# isdigit(): True

# ------------------------------------------
# 19. isalnum() - True if alphabets and digits only
# ------------------------------------------
print("isalnum():", "Python123".isalnum())
# Output:
# isalnum(): True

# ------------------------------------------
# 20. isspace() - True if only spaces
# ------------------------------------------
print("isspace():", "   ".isspace())
# Output:
# isspace(): True

# ------------------------------------------
# 21. center() - Centers the string
# ------------------------------------------
print("center():", "Python".center(20, "-"))
# Output:
# center(): -------Python-------

# ------------------------------------------
# 22. ljust() - Left aligns the string
# ------------------------------------------
print("ljust():", "Python".ljust(15, "-"))
# Output:
# ljust(): Python---------

# ------------------------------------------
# 23. rjust() - Right aligns the string
# ------------------------------------------
print("rjust():", "Python".rjust(15, "-"))
# Output:
# rjust(): ---------Python

# ------------------------------------------
# 24. zfill() - Pads zeros on the left
# ------------------------------------------
print("zfill():", "25".zfill(5))
# Output:
# zfill(): 00025

# ------------------------------------------
# 25. format() - Formats strings
# ------------------------------------------
name = "Shiva"
age = 20
print("My name is {} and I am {} years old.".format(name, age))
# Output:
# My name is Shiva and I am 20 years old.

# ------------------------------------------
# 26. f-string - Modern string formatting
# ------------------------------------------
print(f"My name is {name} and I am {age} years old.")
# Output:
# My name is Shiva and I am 20 years old.

# ------------------------------------------
# 27. partition() - Splits into 3 parts - before, separator and after
# ------------------------------------------
email = "python@gmail.com"
print("partition():", email.partition("@"))
# Output:
# partition(): ('python', '@', 'gmail.com')

# ------------------------------------------
# 28. rpartition() - Splits from the right
# ------------------------------------------
s = "one-two-three-four"
print(s.rpartition("-"))

# Output:
# ('one-two-three', '-', 'four')

print("rpartition():", email.rpartition("@"))
# Output:
# rpartition(): ('python', '@', 'gmail.com')

# ------------------------------------------
# 29. splitlines() - Splits lines into a list
# ------------------------------------------
text = "Hello\nPython\nWorld"
print("splitlines():", text.splitlines())
# Output:
# splitlines(): ['Hello', 'Python', 'World']

# ------------------------------------------
# 30. casefold() - Stronger lowercase conversion
# ------------------------------------------
print("casefold():", "HELLO".casefold())
# Output:
# casefold(): hello

# ------------------------------------------
# 31. encode() - Converts string to bytes
# ------------------------------------------
print("encode():", "Python".encode())
# Output:
# encode(): b'Python'
c = b'\xf0\x9f\x98\x8a'
print(c.decode())
# Output:
# 😊
# ------------------------------------------
# 32. expandtabs() - Converts tabs into spaces
# ------------------------------------------
tab = "Python\tProgramming"
print("expandtabs():", tab.expandtabs(20))
# Output:
# expandtabs(): Python              Programming

# ------------------------------------------
# 33. istitle() - Checks title case
# ------------------------------------------
print("istitle():", "Hello World".istitle())
# Output:
# istitle(): True

# ------------------------------------------
# 34. islower() - Checks lowercase
# ------------------------------------------
print("islower():", "python".islower())
# Output:
# islower(): True

# ------------------------------------------
# 35. isupper() - Checks uppercase
# ------------------------------------------
print("isupper():", "PYTHON".isupper())
# Output:
# isupper(): True

# ------------------------------------------
# 36. removeprefix() - Removes prefix
# ------------------------------------------
url = "https://google.com"
print("removeprefix():", url.removeprefix("https://"))
# Output:
# removeprefix(): google.com

# ------------------------------------------
# 37. removesuffix() - Removes suffix
# ------------------------------------------
filename = "notes.txt"
print("removesuffix():", filename.removesuffix(".txt"))
# Output:
# removesuffix(): notes

# ------------------------------------------
# 38. String slicing examples
# ------------------------------------------
s2 = "helloworld"

print("First 5:", s2[:5])
# Output:
# First 5: hello

print("Last 5:", s2[5:])
# Output:
# Last 5: world

print("Reverse:", s2[::-1])
# Output:
# Reverse: dlrowolleh

print("Every 2nd character:", s2[::2])
# Output:
# Every 2nd character: hlowrd

# ==========================================
# END OF STRING METHODS
# ==========================================