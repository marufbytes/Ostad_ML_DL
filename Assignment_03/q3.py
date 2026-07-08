class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance 

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Error: Balance cannot be negative.")

    def calculate_interest(self, rate, bonus=None):
        if bonus is not None:
            return (self.__balance * rate) + bonus
        else:
            return self.__balance * rate



class ParentA:
    def feature_a(self):
        return "Feature from Parent A"

class ParentB:
    def feature_b(self):
        return "Feature from Parent B"

class ChildClass(ParentA, ParentB):
    def child_feature(self):
        return "Unique Child Feature"



print("\nQ3: Encapsulation & Overloading Testing")

acc = Account("David", 1000)

print(f"Initial Encapsulated Balance (via getter): ${acc.get_balance()}")
acc.set_balance(1200)
print(f"Updated Encapsulated Balance (via setter): ${acc.get_balance()}")

print(f"Interest Calculation (1 parameter - 5%): ${acc.calculate_interest(0.05)}")
print(f"Interest Calculation (2 parameters - 5% + $50 bonus): ${acc.calculate_interest(0.05, 50)}")


print("\n--- Q3: Multiple Inheritance Testing ---")
child_obj = ChildClass()
print(child_obj.feature_a())    
print(child_obj.feature_b())   
print(child_obj.child_feature()) 