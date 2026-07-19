# a countdown using a while loop

count= 5

while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# Building a simple rep counter using a for loop

for rep in range(1,5):
    print(f"This is rep number: {rep}")
    
# A guessing game using a while loop

secret_name = "python"

while True:
    guess = input("Guess the programming language: ")
    
    if guess == secret_name:
        print("Congratulations! You guessed right!!!")
        break
    else:
        print("Sorry, try again.")