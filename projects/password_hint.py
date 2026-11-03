code = input("Enter a code: ").strip()
print(f"Your password hint is: it starts with {code[0].upper()} and ends with {code[-1].upper()}")