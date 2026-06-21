
#Parameterised constructor
class student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

    def show_info(self):
        print(f"{self.name} have cgpa of {self.cgpa}")

s1=student("maruf", 3.5)
s1.show_info()

