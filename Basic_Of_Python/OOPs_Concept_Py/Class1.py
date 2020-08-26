class Student:
    teacher="Dr Adam "
    subject="English"
    def __init__(self,naam,umar,kacha):
        self.name=naam
        self.age=umar
        self.Class=kacha

abhi=Student("Abhi",18,12)
raj=Student("Raj",12,10)

print("Student_1\nStudent Name: ",raj.name,"\nClass Teacher: ",raj.teacher,"\nAge: ",raj.age,"\nClass: ",raj.Class)
print("\nStudemt_2\nStudent Name: ",abhi.name,"\nClass Teacher: ",abhi.teacher,"\nAge: ",abhi.age,"\nClass: ",abhi.Class)
raj.teacher="Shashwat Singh"
raj.subject="Computer Science"

print("\nStudent_1\nStudent Name: ",raj.name,"\nClass Teacher: ",raj.teacher,"\nAge: ",raj.age,"\nClass: ",raj.Class)
print("\nStudemt_2\nStudent Name: ",abhi.name,"\nClass Teacher: ",abhi.teacher,"\nAge: ",abhi.age,"\nClass: ",abhi.Class)

Student.teacher="Shashwat Singh"
Student.subject="Computer Science"
print("\nStudent_1\nStudent Name: ",raj.name,"\nClass Teacher: ",raj.teacher,"\nAge: ",raj.age,"\nClass: ",raj.Class)
print("\nStudemt_2\nStudent Name: ",abhi.name,"\nClass Teacher: ",abhi.teacher,"\nAge: ",abhi.age,"\nClass: ",abhi.Class)
