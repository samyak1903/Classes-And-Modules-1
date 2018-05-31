'''Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.'''
class Student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def display(self):
        ''' display the student details'''
        print("Name={}, RollNumber={}, Age={}, Marks={}".\
              format(self.name,self.rno,self.age,self.marks))
    def setAge(self,age):
        ''' sets the age of student'''
        self.age=age
    def setMarks(self,marks):
        ''' sets the marks of student'''
        self.marks=marks
s1=Student("Amit",1)
s1.setMarks(90)
s1.setAge(20)
s2=Student("Samyak",2)
s2.setMarks(80)
s2.setAge(21)
s1.display()
s2.display()
