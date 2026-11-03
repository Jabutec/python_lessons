# Storing a list of students in a dictionary

students = [
    {"name": "Jabu", "Math": 70, "English": 85, "Science": 90},
    {"name": "Nokuthula", "Math": 65, "English": 90, "Science": 70},
    {"name": "Lesedi", "Math": 60, "English": 78, "Science": 82},
    {"name": "Lebo", "Math": 50, "English": 90, "Science": 55},
    {"name": "Joy", "Math": 90, "English": 60, "Science": 88},
]

results = []
# A loop to iterate over all students and calculate each student's average
for student in students:
    subjects = [student["Math"], student["English"], student["Science"]]
    average = sum(subjects) / len(subjects)
    
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    results.append({"name" : student["name"], "average": average, "grade": grade, "status": status})

total = 0
for result in results:
    total += result["average"]

class_average = total / len(results)
highest_mark = max(result["average"] for result in results)
lowest_mark = min(result["average"] for result in results)
    


# formatted report
print("--------Individual Marks---------")
for result in results:
    print(f"Name: {result['name']}")
    print(f"Average: {result['average']:.2f}")
    print(f"Grade: {result['grade']}")
    print(f"Status: {result['status']}")
    print("-" *15)
print("---------Class Marks------------")
print(f"Class Average: {class_average:.2f}")
print(f"Highest Mark: {highest_mark:.2f}")
print(f"Lowest mark: {lowest_mark:.2f}")

while True:
    search = input("Enter the name of the student(or enter quit to exit: ) ")
    
    if search.lower() == "quit":
        break
    
    found = False
    for result in results:
        if search.strip().lower() == result["name"].lower():
            print(f"Name: {result['name']}")
            print(f"Average: {result['average']:.2f}")
            print(f"Grade: {result['grade']}")
            print(f"Status: {result['status']}")
            found = True
        
    if not found:
        print("There are no records of that name")