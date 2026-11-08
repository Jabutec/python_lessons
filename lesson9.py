# Files and Error Handling
import json

# Part 1: Writing, Appending and Reading(text files)
with open("test1.txt", "w") as test:
    test.write("Welcome")
    
with open("test1.txt", "a") as test:
    test.write("Learning files and error handling")

with open("test1.txt", "r") as test:
    content = test.read()
    print(content)

# Part 2: JSON Files
user = {
    "name": "Jabu",
    "role": "Learner",
    "skils": ["Python", "Files"]
}

with open("data.json", "w") as json_file:
    json.dump(user, json_file, indent=4)
    
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    
# Error handling
try:
    with open("test2.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Could not find file {file}")
    
