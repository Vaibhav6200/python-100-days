a = input("a = ")
b = input("b = ")

print(f"Before Switching: a={a}, b={b}")
a, b = b, a
print(f"After Switching: a={a}, b={b}")