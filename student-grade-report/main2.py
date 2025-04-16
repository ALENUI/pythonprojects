

import os
import json


FILENAME = "./student-grade-report/students.json"

# This class manages student data and grades.
class Student():

# It allows adding new students with new Stud id
    def new_student():
        name = input("Enter Student's Name: ")
        while not name:
                print("Name cannot be empty.")
                name = input("Enter Student's Name: ")
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print("Error reading student data. Please check the file format.")
                return
        else:
            data = {}
        if name in data:
            print("Student already exists.")
            return
        student_id = str(len(data) + 1)
        data[student_id] = {"name": name, "grades": {}}
        with open(FILENAME, "w") as file:
            json.dump(data, file)
        print(f"Student {name} added with ID {student_id}.")
    
   
 # method for adding grades for a student
    def add_grade():
        name = input("Enter Student's Name:")
        while not name:
            print("Name cannot be empty.")
            name = input("Enter Student's Name:") 
        data = {}             
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print("Error reading student data. Please check the file format.")
                return
        else:
            print("No student data found.")
            return
        
        student_id = None
        for key, value in data.items():
            if name.lower() in value["name"].lower():
                student_id = key
                break

        if not student_id:
            print("Student not found.")
            return
        
        def get_valid_grade(subject):
            while True:
                grade = input(f"Enter {subject} grade (0-20): ")
                if grade.isdigit() and 0 <= int(grade) <= 20:
                    return int(grade)
                else:
                    print("Invalid grade. Please enter a number between 0 and 20.")
        
        Math = get_valid_grade("Math")
        Eng = get_valid_grade("English")
        Fren = get_valid_grade("French")
        Phys = get_valid_grade("Physics")
        Chem = get_valid_grade("Chemistry")
        Bio = get_valid_grade("Biology")


        data[student_id]["grades"] = {
            "Math": Math,
            "English": Eng,
            "French": Fren,
            "Physics": Phys,
            "Chemistry": Chem,
            "Biology": Bio
        }
        try: 
            with open(FILENAME, "w") as file:
                json.dump(data, file)
        except IOError:
            print("Error writing to file.")
            return
        print(f"Grades for {name} added successfully. ✅")


# method for calculating average grade for a student
    def calculate_Stud_average():
        name = input("Enter Student's Name: ")
        while not name:
            print("Name cannot be empty.")
            name = input("Enter Student's Name: ")
            
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print("Error reading student data. Please check the file format.")
                return
        else:
            print("No student data found.")
            return
        
        student_id = None
        for key, value in data.items():
            if name.lower() in value["name"].lower():
                student_id=key
                break
        if not student_id:
            print("Student not found.")
            return
        grades = data[student_id]["grades"]
        if not grades:
            print("No grades found for this student.")
            return
       
        grades = [int(grade) for grade in grades.values()]
        average = sum(grades) / len(grades)
        data[student_id]["average"] = average
        try:
            with open(FILENAME, "w") as file:
                json.dump(data, file)
        except IOError:
            print("Error writing to file.")
            return
        print(f"Grades for {name}: {grades}")
        print(f"Average grade for {name} is {average:.2f}.")

        
# method for displaying all students and their grades
    def display_all_students():
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print("Error reading student data. Please check the file format.")
                return
        else:
            print("No student data found.")
            return
        for student_id, student_data in data.items():
            name = student_data["name"]
            grades = student_data["grades"]
            average = student_data.get("average", "N/A")
            print(f"ID: {student_id}, Name: {name}, Grades: {grades}, Average: {average}")
        


def menu():
    print("\n ========= MENU =========== \n")
    print("1. Add New Student")
    print("2. Add Grades")
    print("3. Calculate Average Grade")
    print("4. Display All Students")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

print ("\n Welcome to the Student Management System")
while True:
    choice = menu()
    print("\n")
    if choice == "1":
        Student.new_student()
    elif choice == "2":
        Student.add_grade()
    elif choice == "3":
        Student.calculate_Stud_average()
    elif choice == "4":
        Student.display_all_students()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
