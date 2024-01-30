# Define the base class 'employee' with common attributes and a display method
class employee():
    def __init__(self, ecode, name, email, address):
        self.ecode = ecode
        self.name = name
        self.email = email
        self.address = address
        
    def display(self):
        print("\nEmployee Code", self.ecode)
        print("Employee Name", self.name)
        print("Employee Email", self.email)
        print("Employee Address", self.address)

# Define a derived class 'RegEmp' inheriting from 'employee' with additional salary-related methods
class RegEmp(employee):
    def __init__(self, ecode, name, email, address, salary):
        super().__init__(ecode, name, email, address)
        self.salary = salary
    
    def Gross_salary(self):
        tax = 0.1 * self.salary
        return self.salary - tax
    
    def RegEmpDis(self):
        super().display()
        print("Employee Salary", self.salary)
        print("Employee Gross Salary")
        print(self.Gross_salary())

# Define another derived class 'WageEmp' inheriting from 'employee' with wage-related methods
class WageEmp(employee):
    def __init__(self, ecode, name, email, address, wage):
        super().__init__(ecode, name, email, address)
        self.wage = wage
        
    def monthly_salary(self):
        return 30 * self.wage
    
    def WageEmpDis(self):
        super().display()
        print("Employee Wage", self.wage)
        print("Employee Monthly Salary")
        print(self.monthly_salary())

# Main program for ABC Corp Payroll System
print("Welcome ABC Corp Payroll System\n1.Reg Employee\n2. Wage Employee")
choice = int(input("Enter the Choice\n"))

# Branch based on the user's choice
if choice == 1:
    ecode = int(input("Enter the Employee Code "))
    name = input("Enter the Name ")
    email = input("Enter the Email ")
    address = input("Enter the Address ")
    salary = float(input("Enter the Salary "))
    emp = RegEmp(ecode, name, email, address, salary)
    emp.RegEmpDis()

elif choice == 2:
    ecode = int(input("Enter the Employee Code "))
    name = input("Enter the Name ")
    email = input("Enter the Email ")
    address = input("Enter the Address ")
    wage = float(input("Enter the Wage "))
    emp = WageEmp(ecode, name, email, address, wage)
    emp.WageEmpDis()
