class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade
    
    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if new_grade<0:
            print("invalid grade. Must be between 0a dn 20")
        elif 0<=new_grade<=20:
            self.__grade = new_grade

    def to_dict(self):
        return {"name": self.__name, "grade": self.__grade}