def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
if exponent < 0:
    print("Negative exponents are not supported.")
else:
    print(f"{base}^{exponent} = {power(base, exponent)}")