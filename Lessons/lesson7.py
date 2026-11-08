# creating a simple function
def greet_user():
    print("Welcome to the application")
    
# calling the our function
greet_user()

# Defining a function with a parameter
def vat_calculator(amount):
    tax = amount * 0.15
    print(f"The vat for the amount R{amount} is {round(tax,2)}")
    
# calling the funtion
vat_calculator(100)
vat_calculator(250)

# calculating using a function
def add_numbers(num1, num2):
    total = num1 + num2
    return total

# calling the function
total_even = add_numbers(2,4)
total_odd = add_numbers(1,3)

print(total_even)
print(total_odd)