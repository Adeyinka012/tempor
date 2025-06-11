# class Student:
#     age = 15
#     def _init_(self, name ,grade, school):
#         self.name=name
#         self.grade=grade
#         self.school=school

#     def intro(self):
#         print(f"The student name is{self.name} he is in grade {self.grade} at {self.school}")
    
# stud=Student("Zakir", 7, "codingal")
# stud.intro()
# print(stud.age)

class Student:
    age = 15
    def __init__(self, name, grade, school):
        self.name=name
        self.grade=grade
        self.school=school
        
    def intro(self):
        print(f"The student name is{self.name} he is in grade{self.grade} at {self.school}")

stud=Student("Fareed", 8, "codingal")
stud.intro()
print(stud.age)