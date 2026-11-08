# Tracking individual letters
name = "Jabulani"
print(name[0]) # This is the first letter in the name
print(name[-1]) # -1 starts from the end of the name so this becomes "i"
print(name[1]) # This is the second letter of the name


# using string methods
city = " Johannesburg "
print(city.upper()) # The method upper() returns the word in all Capital letters
print(city.strip()) # The method strip() returns the word without spaces before and after the word
print(city.lower()) # This method return the word in lower cases
print(city.title()) # This method returns the word in title(Only the first letter in Uppercase) case


# combining strings
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

username = f"{first_name[0]}{last_name}"

print(f"Your email is {username.lower()}@university.co.za")