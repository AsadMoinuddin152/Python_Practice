class employee():
    jobs=[]
    def __init__(self, name, email, status):
        self.name = name
        self.email =  email
        self.status = status
        self.jobs.append(self)
    
    def display(self):
        print(len(self.jobs))

while True:
    choice = int(input("Enter the Choice \n1: Enter new Job\n2:Display Entries"))
    if choice == 1:
        name = input("Enter the Name ")
        email = input("Enter the Email ")
        status = input("Enter the Status ")
        emp = employee(name, email, status)
        
    elif choice == 2:
        emp.display()
    
    else:
        break