cart = [("Pen", 10), ("Book", 50), ("Bag", 500)]
total = cart[0][1] + cart[1][1] + cart[2][1]
most_expensive = max(cart, key=lambda x: x[1])
cheapest = min(cart, key=lambda x: x[1])
print(f"Total Bill: {total}")
print(f"Most Expensive: {most_expensive[0]}")
print(f"Cheapest: {cheapest[0]}")