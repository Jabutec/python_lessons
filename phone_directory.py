# A dictionary of friends' contacts

contacts = {
    "Thabo": "0725327152",
    "Lebo" : "0835347153",
    "Thuli": "0635537243"
}

search = input("Enter the name of the friend you want to look up: ").title()

if search in contacts:
    print(f"Found! {search}'s number is {contacts[search]}")
else:
    print("Contact not found.")