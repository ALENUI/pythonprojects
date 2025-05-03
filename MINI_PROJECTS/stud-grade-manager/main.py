import csv
from student import Student

FILENAME ="./MINI_PROJECTS/stud-grade-manager/studFile.csv"
students=[]
#loead data from csv

with open(FILENAME, "r") as file:
    data = csv.DictReader(file)
    for row in data:
        students.append(Student(row['name'], int(row["grade"])))


print("Current Grade: ")
for s in students:
    print(f"{s.get_name()}:  {s.get_grade()}")

target_name =  input("\n Enter name to update grade: ")
for s in students:
    if s.get_name.lower() == target_name.lower():
        new_grade=int(input("enter New grade: "))
        s.set_grade(new_grade)
        break
else:
    print("Student not found")


with open(FILENAME, "w", newline="") as file:
    fieldnames = ["name", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for s in students:
        writer.writerow(s.to_dict())
print("\n Grade updated successfuly")