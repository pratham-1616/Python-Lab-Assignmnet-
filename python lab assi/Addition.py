n1 = float(input("Enter the first number:  "))
n2 = float(input("Enter the second number: "))

addition = n1 + n2 
subtriction = n1 - n2 
multiplication = n1 * n2 
divison = n1 / n2 if n2 != 0 else "undefined (does not divide by zero)"

print(f"Addition: {addition}")
print(f"Subtriction: {subtriction}")
print(f"multiplication: {multiplication}")
print(f"divison: {divison}")