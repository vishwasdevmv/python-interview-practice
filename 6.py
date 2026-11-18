class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def print_student_info(self):
        print(f"Student name: {self.name}")
        print(f"Student age: {self.age}")
        print(f"Student gender: {self.gender}")

student1 = Student("Ram", 16, "Male")
student2 = Student("Raheem", 19, "Male")


#student1.print_student_info()
#student2.print_student_info()
student1.get_name()