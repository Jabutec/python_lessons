from ZOO import Zoo

def main():

    menu = """
    What would you like to do?
        1. Visit an Animal
        2. Show an animal
        3. Add an animal
        4. Quit
    choice: """    
    
    while True:
        choice = input(menu).strip()
        
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            print("Thank you for visiting the Zoo, Goodbye")
            break
        else:
            print("Invalid choice, please enter a number between (1-4).\n")
main()
