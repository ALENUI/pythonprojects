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
        
        data[employee_id] = {"name": name, "salary": salary}

        try:
            with open(FILENAME, "w") as file:
                json.dump(data, file)
            print("Employee added! ")
        except Exception as e:
            print(f"error with {e}")
            return
        

Employee.add_employee()