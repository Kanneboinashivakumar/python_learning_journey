nums = [10, 25, 40, 55]
num_to_check = int(input("Enter number to search: "))
print(f"Max: {max(nums)}")
print(f"Min: {min(nums)}")
if num_to_check in nums:
    print(f"{num_to_check} exists in list")
else:
    print(f"{num_to_check} not found")