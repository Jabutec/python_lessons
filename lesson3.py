# arithmetic operations

num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))

print(f"Addition: {round(num1 + num2, 2)}")
print(f"Subtraction: {round(num1 - num2, 2)}")
print(f"Multiplication: {round(num1 * num2, 2)}")
print(f"Division: {round(num1 / num2, 2)}")
print(f"Modulus: {round(num1 % num2, 2)}")
print(f"floor Division: {round(num1 // num2, 2)}")

if num2 == 0 :
    print("Cannot divide by zero")
else :
    print(f"Division: {round(num1 / num2, 2)}")