kilometers = int(input("Enter the distance in kilometers: "))
price_per_liter = float(input("Enter the price of fuel per liter: "))

litters_needed = kilometers / 10  # Assuming the car consumes 1 liter per 10 kilometers

print(f"total cost of fuel: {round(litters_needed * price_per_liter, 2)}")