
from abc import ABC, abstractmethod 
  
class user(ABC): 
    def __init__(self,name,joining_year):
         self.name=name
         self.joining_year=joining_year
  

    def years_platform(self): 
        return  2025 - self.joining_year
    @abstractmethod
    def show_role(self):
        pass

class customer(user):
    def show_role(self):
        return "customer"
    def display(self):
        print(f"Name: {self.name}, Role: {self.show_role()}, Years on Platform: {self.years_platform()}")
class Vendor(user):
    def show_role(self):
        return "Vendor"

    def display(self):
        print(f"Name: {self.name}, Role: {self.show_role()}, Years on Platform: {self.years_platform()}")


c1 = customer("Anu", 2020)
v1 = Vendor("Ravi", 2018)

c1.display()
v1.display()