import os
import json
FILENAME = "./MINI_PROJECTS/employee-management/employees.json"

class Employee:
    
    def add_employee():
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print("Error reading account data. Please check the file format.")
                return
        else:
            data= {}

        employee_id = str(len(data) + 101)
        name = input("Enter Employee name: ")
        while not name:
            print("name cannot be empty. ")
            name = input("Enter Employee name: ")
        if name in data:
            print("employee Name already exist.")
            name=input("Input New Name: ")
        salary = input("Enter Base salary: ")
        while not salary.isdigit():
            print("salary must be number")
            salary = input("Enter Base salary: ")
        cat = input("Enter Category: ")
        while not cat:
            print("Category cannot be empty.")
            cat = input("Enter Category (Manager/Dev) : ")
        if cat not in ["Manager", "Dev"]:
            print("Invalid category. Please enter either 'Manager' or 'Dev'.")
            return
        if cat == "Manager":
            bonus = 0.6 * int(salary)
        elif cat == "Dev":
            bonus = 0.4 * int(salary)
        
        data[employee_id] = {"name": name, "salary": salary, "category": cat, "bonus": bonus}
       

        try:
            with open(FILENAME, "w") as file:
                json.dump(data, file)
            print(f"New Employee Added. \nEmployee ID: {employee_id}, Name: {name}, Salary: {salary}, Category: {cat}, Bonus: {bonus}")
        except Exception as e:
            print(f"error with {e}")
            return
        
    def view_employee():
        if os.path.exists(FILENAME):
            try:
                with open(FILENAME, "r") as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                print("Error reading account data. Please check the file format.")
                return
        else:
            print("No employee data found.")
            return

        if not data:
            print("No employee data found.")
            return

        for emp_id, emp_data in data.items():
            print(f"ID: {emp_id}, Name: {emp_data['name']}, Salary: {emp_data['salary']}, Category: {emp_data['category']}, Bonus: {emp_data['bonus']}")
        print("Total Employees: ", len(data))



Employee.add_employee()
Employee.view_employee()