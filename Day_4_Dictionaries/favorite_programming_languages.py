user1 = {"Python", "Java", "C", "JavaScript"}
user2 = {"Python", "C++", "JavaScript", "Go"}

common_languages = user1.intersection(user2)

print("User 1 Favorites:", user1)
print("User 2 Favorites:", user2)

if common_languages:
    print("Common Favorite Languages:", common_languages)
else:
    print("No common favorite languages found")