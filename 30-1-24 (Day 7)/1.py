class Node:
    def __init__(self, data):
        # Initialize a node with data, a reference to the previous node, and a reference to the next node
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # Initialize an empty doubly linked list with head and tail set to None
        self.head = None
        self.tail = None

    def append(self, data):
        # Add a new node with the given data to the end of the doubly linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            self.tail = new_node

    def find_max(self):
        # Find and return the maximum value in the doubly linked list
        if self.head is None:
            return None
        else:
            current = self.head
            max_num = current.data
            while current:
                if current.data > max_num:
                    max_num = current.data
                current = current.next
            return max_num

    def display(self):
        # Display the elements of the doubly linked list from head to tail
        if self.head is None:
            print("Doubly linked list is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end="")
                if current.next:
                    print("-->", end="")
                current = current.next
            print()
    
    def display_reverse(self):
        # Display the elements of the doubly linked list from tail to head
        if self.head is None:
            print("Doubly linked list is empty.")
        else:
            current = self.tail
            while current:
                print(current.data, end="")
                if current.prev:
                    print("-->", end="")
                current = current.prev
            print()

# Create a DoublyLinkedList instance
dll = DoublyLinkedList()

# Append elements to the doubly linked list
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)

# Find and display the maximum number in the doubly linked list
max_num = dll.find_max()
print("Maximum number:", max_num)

# Display the elements of the doubly linked list from head to tail
dll.display()

# Display the elements of the doubly linked list from tail to head
dll.display_reverse()
