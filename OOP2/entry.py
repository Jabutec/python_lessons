from ZOO import Zoo

def main():

    menu = """
    What would you like to do?
        1. Visit an Animal
        2. Show an animal
        3. Add an animal
        4. Quit
    choice: """    
    Z1 = Zoo("Midvall Zoo", 250)
    while True:
        choice = input(menu).strip()
        
        if choice == "1":
            pass
        elif choice == "2":
            {
                "animalType": "Lion",
                "animalName": "Bob",
                "animalAge": 12,
                "claws" : 10
            }
            
            aType = input("Enter the animal type: ").strip()
            aName = input("Enter the animal name: ").strip()
            aAge = input("Enter the animal age: ").strip()
            
            if aType == "Lion":
                aClaw = input("Enter the number of claws: ").strip()
                
                dictAnimal ={
                    "animalType": aType,
                    "name": aName,
                    "age": aAge,
                    "claws" : aClaw
                }
                
            elif aType == "Snake":
                aVpotent = input("Enter the number of vpotent: ").strip()
                            
                dictAnimal ={
                    "animalType": aType,
                    "name": aName,
                    "age": aAge,
                    "vpotent" : aVpotent
                }
                
            elif aType == "Zebra":
                stripes = input("Enter the number of stripes: ").strip()
                            
                dictAnimal ={
                    "animalType": aType,
                    "name": aName,
                    "age": aAge,
                    "stripes" : stripes
                }
                
                
                
                Z1.addAnimal(dictAnimal)
                
                for animal in Z1.animals:
                    animal.makeSound()
            
        elif choice == "3":
            pass
        elif choice == "4":
            print("Thank you for visiting the Zoo, Goodbye")
            break
        else:
            print("Invalid choice, please enter a number between (1-4).\n")
            
main()
