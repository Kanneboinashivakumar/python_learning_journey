def nested_sum(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total

numbers = [1, 2, [3, 4], [5, [6, 7]], 8]

print("List:", numbers)
print(f"Total Sum: {nested_sum(numbers)}")