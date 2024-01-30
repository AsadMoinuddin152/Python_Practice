# Define the 'employee' class with a class variable 'jobs' to store instances
class employee():
    jobs = []

    def __init__(self, name, email, status):
        self.name = name
        self.email = email
        self.status = status
        # Append each instance to the class variable 'jobs'
        self.jobs.append(self)
    
    # Method to display the number of entries in 'jobs'
    def display(self):
        print(len(self.jobs))

# Main program loop
while True:
    # User input for choice
    choice = int(input("Enter the Choice \n1: Enter new Job\n2: Display Entries"))
    
    if choice == 1:
        # Get details for a new job and create an instance of 'employee'
        name = input("Enter the Name ")
        email = input("Enter the Email ")
        status = input("Enter the Status ")
        emp = employee(name, email, status)
        
    elif choice == 2:
        # Display the number of entries in 'jobs'
        emp.display()
    
    else:
        # Exit the loop if choice is neither 1 nor 2
        break
