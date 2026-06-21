class person:
    def __init__(self, name, age):
        self.name = name
        self.age =age

    def greet(self):
        print(f"Hi! I am {self.name}, age {self.age}")


class student(person):
    def study(self):
        print(f"{self.name} is studying Python")

s = student("Maruf", 22)
print(s.name)
print(s.age)

s.greet()
s.study()