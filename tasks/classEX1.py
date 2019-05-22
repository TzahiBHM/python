class Student:
    sumGrade =0
    sumAge=0
    sumStudent=0
    def __init__(self,age, grade):
        self.age = age
        self.grade = grade
        Student.sumGrade = Student.sumGrade + grade
        Student.sumAge = Student.sumAge + age
        Student.sumStudent +=1
    @classmethod
    def AvgGrade(self):
        print(Student.sumGrade/Student.sumStudent)
    @classmethod
    def AvgAge(self):
        print(Student.sumAge / Student.sumStudent)
 
 
s1 = Student(18,100)
s2 = Student(24,60)
s3 = Student(50,40)
s4 = Student(27,85)
#s1 details
print(s1.grade,s1.age)
#s2 details
print(s2.grade,s2.age)
#s3 details
print(s3.grade,s3.age)
#s4 details
print(s4.grade,s4.age)  # --> 27,85
 
#print average of students grades
print("Average grades: ")
Student.AvgGrade()
#print average of students age
print("Average age:")
Student.AvgAge()