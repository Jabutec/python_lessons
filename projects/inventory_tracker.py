
# End of the week practice
inventory = [
    
    {"name": "apples" , "quantity": 20, "price": 3.50 , "category": "fresh produce" },
    {"name": "berries" , "quantity": 50, "price": 20.50 , "category": "fresh produce" },
    {"name": "Bread" , "quantity": 100, "price": 22.50 , "category": "Bakery" },
    {"name": "Chicken" , "quantity": 80, "price": 120.00 , "category": "Meat"},
    {"name": "milk" , "quantity": 20, "price": 22.50 , "category": "Dairy"},
    {"name": "water" , "quantity": 20, "price": 10.00 , "category": "Beverages" },
    {"name": "tissues" , "quantity": 20, "price": 30.50 , "category": "Cleaning" },
]

while True:
    print("\n-------Menu--------")
    print("1. Add Item")
    print("2. View All Inventory")
    print("3. View by Category")
    print("4. Update Quantity")
    print("5. Search Item")
    print("6. Delete item")
    print("7. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        name = input("Enter the name of the item: ").strip()
        quantity = int(input("Enter the quantity of the items: ").strip())
        price = float(input("Enter the price of the item: ").strip())
        category = input("Enter the category of the item: ").strip()
        
        new_item = {"name": name, "quantity": quantity, "price": price , "category": category }
        inventory.append(new_item)
        
        print(f"{name} has been added successfully")
        
    elif choice == "2":
        print("-------All Inventory------")
        for items in inventory:
            print(f"Name: {items['name']}")
            print(f"Quantity: {items['quantity']}")
            print(f"Price: {items['price']}")
            print(f"Category: {items['category']}")
            print("-" *20)
    
    elif choice == "3":
        print("------Categories-------")
        for category in inventory:
            print(f"Category: {category['category']}")
            
    elif choice == "4":
        name = input("Enter the name of the item to update: ").strip().lower()
        
        found = False
        for items in inventory:
            if items['name'].lower() == name.lower():
                found = True
                action = input("Add or remove stock (add/remove): ").lower()
                amount = int(input("Enter quantity: ").stip())
                
                if action == "add":
                    items["quantity"] += amount
                elif action == "remove":
                    items["quantity"] -= amount
                    
                print(f"Items {items['name']} has been updated!")
        
        if not found:
            print("Item not found")
            
    elif choice == "5":
        search = input("Enter the name of the item you want to search: ").strip().lower()
        
        found = False
        for items in inventory:
            if search.lower() == items["name"].lower():
                print(f"Name: {items['name']}")
                print(f"Quantity: {items['quantity']}")
                print(f"Price: {items['price']}")
                print(f"Category: {items['category']}")
                print("-" *20)
                found = True
        if not found:
            print("Item not found")
            
    elif choice == "6":
        delete = input("Enter the name of the item you want to delete: ").strip().lower()
        
        found = False
        remaining = []
        for items in inventory:
            if delete.lower() == items["name"].lower():
                inventory.remove(items)
                found = True
            else:
                remaining.append(items)
            
        inventory = remaining
        
        if found:
            print(f"{delete} has been deleted")
        else:
            print("Item not found")
                
    elif choice == "7":
        print("Exiting....")
        break
    else:
        print("Invalid choice, Try again")