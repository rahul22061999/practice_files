class Student:
    def __init__(self, name, age,grade):
        self.name = name
        self.age = age 
        self.grade = grade
    def student_grade(self):
        return self.grade 
    
class Course:
    def __init__(self, name, max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True 
        return False 
    def avg_grade(self):
        pass 

s1 = Student("Tim", 20, 95)
s2 = Student("Cook", 19, 70)
s3 = Student("Steve", 21, 55)

course = Course("Math",2)
course.add_student(s1)
course.add_student(s2)

print(course.students[1].name)