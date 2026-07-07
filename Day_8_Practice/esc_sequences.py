# ==========================================
# PYTHON ESCAPE SEQUENCES
# ==========================================

# ------------------------------------------
# 1. \n - New Line
# ------------------------------------------
print("Hello\nPython")

# Output:
# Hello
# Python

# ------------------------------------------
# 2. \t - Tab Space
# ------------------------------------------
print("Hello\tPython")

# Output:
# Hello    Python

# ------------------------------------------
# 3. \\ - Prints a Backslash
# ------------------------------------------
print("C:\\Users\\Shiva")

# Output:
# C:\Users\Shiva

# ------------------------------------------
# 4. \' - Prints a Single Quote
# ------------------------------------------
print('It\'s Python')

# Output:
# It's Python

# ------------------------------------------
# 5. \" - Prints a Double Quote
# ------------------------------------------
print("He said \"Hello\"")

# Output:
# He said "Hello"

# ------------------------------------------
# 6. \b - Backspace (Deletes Previous Character)
# ------------------------------------------
print("ABC\bD")

# Output:
# ABD

# ------------------------------------------
# 7. \r - Carriage Return (Moves Cursor to Beginning)
# ------------------------------------------
print("Hello\rHi")

# Output:
# Hillo

# ------------------------------------------
# 8. \a - Alert/Bell (May Produce a Beep)
# ------------------------------------------
print("Hello\a")

# Output:
# Hello
# (May produce a beep depending on the system)

# ------------------------------------------
# 9. \f - Form Feed (Page Break)
# ------------------------------------------
print("Hello\fWorld")

# Output:
# HelloWorld
# (May create a page break in some terminals ,internally looks like-'Hello\x0cWorld')

# ------------------------------------------
# 10. \v - Vertical Tab
# ------------------------------------------
print("Hello\vWorld")

# Output:
# Hello
#      World
# (Appearance depends on the terminal)

# ------------------------------------------
# 11. Raw String - Ignores Escape Sequences
# ------------------------------------------
path = r"C:\Users\Shiva\Documents"

print(path)

# Output:
# C:\Users\Shiva\Documents

# ------------------------------------------
# 16. Without Raw String
# ------------------------------------------
path = "C:\new\test"

print(path)

# Output:
# C:
# ew	est

