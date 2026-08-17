class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_details(self):
        print("name:",self.name)
        print("age:",self.age)

class Employee(Person):
    def __init__(self,name,age,employee_id):
              self.name=name
              self.age=age
              self.employee_id=employee_id
    def show_details(self):
         print("name:",self.name)
         print("age:",self.age)
         print("employee_id:",self.employee_id)
class PartTime(Person):
    def __init__(self,name,age,working_hours):
              super().__init__(name, age)
              self.working_hours = working_hours
              self.working_hours=working_hours

    def show_details(self):
         print("Name:", self.name)
         print("Age:", self.age)
         print("Working Hours:", self.working_hours)
class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name
    
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Working Hours:", self.working_hours)
        print("Project Name:", self.project_name)

person1 = Person("Anu", 25)
employee1 = Employee("Rahul", 30, "E101")
parttime1 = PartTime("Meera", 22, 4.5)
consultant1 = Consultant("Vivek", 35, "C201", 6.0, "Website Development")


print("Person Details")
person1.show_details()

print("\nEmployee Details")
employee1.show_details()

print("\nPartTime Details")
parttime1.show_details()

print("\nConsultant Details")
consultant1.show_details()    