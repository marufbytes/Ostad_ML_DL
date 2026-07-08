class Student:

    def __init__(self, name="Unknown", student_id="Not Assigned"):
        self.name = name
        self.id = student_id

    def display_details(self):
        print(f"Student Name: {self.name} | ID: {self.id}")

    def future_feature_placeholder(self):
        pass


print(" Q1: Student Class Testing")

student1 = Student()
print("Object 1 (Default):")
student1.display_details()

student2 = Student("Alice Smith", "S10234")
print("\nObject 2 (Parameterized):")
student2.display_details()