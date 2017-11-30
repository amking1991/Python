class Student:

#####Method ( must right "self")########
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

student1 = Student ("King", 85)
student2 = Student ("Anthony", 85)

print(student1.name)
print(student2.name)
print(student1.grade)
print(student2.grade)
