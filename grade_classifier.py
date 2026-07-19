# get inputs, name and marks for three subjects

name = input("Enter your name: ")
math = float(input("Enter your marks for Mathematics: "))
science = float(input("Enter your marks for Science: "))
english = float(input("Enter your marks for English: "))

# store marks in a dictionary
marks = { "Mathematics": math, "Science": science, "English": english }

# calculate the average
average = sum(marks.values()) / len(marks)


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

#assign pass/fail status based on average marks
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# Subjects that need intervention (marks below 40)
intervention_subjects = []
for subject, mark in marks.items():
    if mark < 40:
        intervention_subjects.append(subject)

# display the report card
print(f"Report Card for {name}:")
for subject, mark in marks.items():
    print(f"{subject}: {mark}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
print(f"Status: {status}")

if intervention_subjects:
    print("Subjects that need intervention:")
else:
    print("No subjects need intervention.")