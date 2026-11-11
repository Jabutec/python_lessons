import json

# The name of the text file you must create. Do not change it -
# the marker looks for this exact filename.
OUTFILE = "calculations.txt"


def saveJsonFile():
    try:
        with open("newZooAnimals.json", "w") as NZA:
            toStore = [
                {"name": "bob", "age": 20, "species": "crocodile"},
                {"name": "susan", "age": 10, "species": "pigeon"},
            ]
            json.dump(toStore, NZA)
    except FileNotFoundError as Fnf:
        print(f"Could not find file {Fnf.filename}")


def saveTextFile(multiple, valueArray, value2):
    # TODO 1: Start with 'multiple' and multiply it by every value in
    # valueArray, then divide that answer by value2.
    # For example: 5 with [1, 3, 5, 7] and value2 = 2
    #              gives 5*1*3*5*7 = 525, then 525 / 2 = 262.5

    result = None
    for v in valueArray:
        multiple *= v

    if value2 == 0:
        print("Cannot devide by zero!")
        return

    result = multiple / value2

    try:
        with open(OUTFILE, "w") as file:
            file.write(f"Starting number: {multiple}\n")
            file.write(f"Values: {valueArray}\n")
            file.write(f"Final answer: {result}\n")
    except FileNotFoundError as FNE:
        print(f"could not find file {FNE.filename}")

    # TODO 2: Write the multiple used, the full list of values, and the
    # final answer into the file named by OUTFILE.
    # Wrap the file handling in a try/except block and print a friendly
    # message instead of crashing.

    # Hint: remember it is not possible to divide by 0, so that is a
    # pitfall to look out for. If value2 is 0, print a message and
    # write nothing.

    # Hint: opening a file in 'w' mode replaces whatever was there before.
    # Consider which mode you actually want.

    pass


def readTextFile(filename):
    # TODO 3: Open the text file you just made and read from it.
    # Wrap it in a try/except block and print a friendly message if the
    # file does not exist.

    # TODO 4: Once you have the contents, print them out to the terminal.
    # Think about how to loop through them and print each one nicely.
    try:
        with open(filename, "r") as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError as FNE:
        print(f"Could not find file {FNE.filename}")
    pass


def demo():
    saveTextFile(5, [1, 3, 5, 7], 2)
    readTextFile(OUTFILE)

    # TODO 5: Call saveTextFile with a value2 that is not zero, then
    # display the contents of the file in the terminal.


demo()
