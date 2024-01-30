class Node:
    def __init__(self, data):
        # Initialize a node with data and a reference to the next node
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        # Initialize an empty stack with the top set to None
        self.top = None
    
    def push(self, data):
        # Add a new node with the given data to the top of the stack
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            current = self.top
            while current.next:
                current = current.next
            current.next = new_node
            
    def check_empty(self):
        # Check if the stack is empty
        if self.top is None:
            return True
        else:
            return False
        
    def pop(self):
        # Remove the top element from the stack
        self.check_empty()
        current = self.top
        while current.next:
            current = current.next
        current.next = None
    
    def peek(self):
        # Return the top element of the stack without removing it
        self.check_empty()
        current = self.top
        while current.next:
            current = current.next
        return current.data
    
    def display(self):
        # Display the elements of the stack
        self.check_empty()
        current = self.top
        while current:
            print(current.data, end="")
            if current.next:
                print("-->", end="")
            current = current.next
        print()
    
    def min_element(self):
        # Find and return the minimum element in the stack
        self.check_empty()
        current = self.top
        min = current.data
        while current:
            if current.data < min:
                min = current.data
            current = current.next
        return min
    
# Create a Stack instance
S1 = Stack()

# Push elements onto the stack
S1.push(40)
S1.push(30)
S1.push(3)
S1.push(20)
S1.push(10)

# Display the elements of the stack
S1.display()

# Peek at the top element of the stack
print(S1.peek())

# Pop an element from the stack
S1.pop()

# Display the elements of the updated stack
S1.display()

# Peek at the top element of the updated stack
print(S1.peek())

# Find and display the least element in the stack
print(f"Least Element: {S1.min_element()}")
