#  This code is a simple student grade report system that allows adding grades for different subjects and calculating the average grade. It also provides a visual representation of whether the student has passed or failed in each subject.

class Student():
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, score):
        try:
            if 0 <= score <= 100:
                self.grades[subject] = score
                print(f"Added {score} for {subject} to {self.name}'s record.")
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        
    def get_average(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        else:
            return 0.0
        
    def print_report(self):
        print(f"Report for {self.name}:")
        for subject, score in self.grades.items():
            status = " ✅ " if score >= 50 else "❌"
            print(f"{subject}: {score} - {status}")
        average = self.get_average()
        print(f"Average: {average:.2f}")
    

student1 = Student("Alenui")

student1.add_grade("Maths", 90)
student1.add_grade("Python", 88)
student1.add_grade("Data Science", 45)

student1.print_report()