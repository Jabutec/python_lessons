
contacts = []

while True:
    print("\nContact Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        name = input("Enter your name: ").title()
        phone = input("Enter your phone number: ")
        email = input("Enter your email address: ") 

        contact_info = {"Name": name, "Phone": phone, "Email": email}
        contacts.append(contact_info)
    
        print(f"Contact {name} has been added successfully.")
        
    elif choice == "2":
        print("\nContact List:")
        for contact in contacts:
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print("-" * 20)
            
    elif choice == "3":
        search_contact = input("Enter the name of the contact you want to search for: ").title()

        if search_contact:
            found = False
            for contact in contacts:
                if contact["Name"].title() == search_contact:
                    print(f"Contact found: {contact}")
                    found = True
            if not found:
                print("Contact not found.")
                
    elif choice == "4":
        delete_contact = input("Enter the name of the contact you want to delete: ").title()

        Found = False
        if delete_contact:
            for contact in contacts:
                if contact["Name"].title() == delete_contact:
                    contacts.remove(contact)
                    print(f"Contact {delete_contact} has been deleted.")
                    Found = True
            if not Found:
                print("Contact not found.")
    
    elif choice == "5":
        print("Exiting....")
        break
    else:
        print("Invalid choice. Please try again.")
        
# this dee