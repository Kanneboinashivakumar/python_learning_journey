s1 = ("Shiva", 85)
s2 = ("Ram", 90)
if s1[1] > s2[1]:
    print(f"{s1[0]} scored higher than {s2[0]}")
elif s1[1] < s2[1]:
    print(f"{s2[0]} scored higher than {s1[0]}")
else:
    print("Both have equal marks")