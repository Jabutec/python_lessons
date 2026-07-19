# Inputs: name, surname, age, favourable_number
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourable_number = float(input("Enter your favourite number: "))

# outputs
print(f"Welcome, {first_name} {surname}!")
print(first_name.upper(), first_name.title())
print( age * 12)
print(round(favourable_number, 2))

# Data types
print(type(first_name))
print(type(surname))
print(type(age))
print(type(favourable_number))