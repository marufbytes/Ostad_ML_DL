class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I am {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id

    def introduce(self):
        return f"Hi, I am {self.name} (ID: {self.student_id}), a student."

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, research_topic):
        super().__init__(name, age, student_id)
        self.research_topic = research_topic

    def introduce(self):
        return f"Hi, I am {self.name}. I am a graduate student researching '{self.research_topic}'."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"Hello, I am Professor {self.name}, and I teach {self.subject}."



print("\nQ2: Inheritance Testing")

person = Person("John", 45)
student = Student("Emma", 20, "STU99")
grad_student = GraduateStudent("Liam", 25, "GRAD44", "Machine Learning")
teacher = Teacher("Dr. Sarah", 38, "Computer Science")

print("Base Person:        ", person.introduce())
print("Single (Student):   ", student.introduce())
print("Multilevel (Grad):  ", grad_student.introduce())
print("Hierarchical (Teach):", teacher.introduce())