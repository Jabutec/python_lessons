first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
bio = input("Enter a short bio about yourself: ").strip()

username = f"{first_name[0]}{last_name}"
print(f"Your full name is: {first_name.title()} {last_name .title()}")

print(len(bio))
updated_bio = bio.replace("I am", "I'm")
print(f"Your updated bio is: {updated_bio}")

print(f"Your name username is: {username.lower()} and your bio is: {updated_bio}")
