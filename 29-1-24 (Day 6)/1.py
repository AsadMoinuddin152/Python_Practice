# Define a Node class for a linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a LinkedList class with methods for appending, prepending, displaying, and counting elements
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        # Add a new node to the end of the linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        # Add a new node to the beginning of the linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def display(self):
        # Display the elements of the linked list
        current = self.head
        print("Display of Elements:")
        while current:
            print(current.data, end="")
            if current.next:
                print("-->", end="")
            current = current.next
        print()

    def count(self, element):
        # Count the occurrences of a specific element in the linked list
        count = 0
        current = self.head
        while current:
            if current.data == element:
                count += 1
            current = current.next
        return count

# Create an instance of the LinkedList class
linked_list = LinkedList()

# Append and prepend elements to the linked list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
linked_list.append(2)
linked_list.append(3)

# Display the elements of the linked list
linked_list.display()

# Count the occurrences of the element 2 in the linked list
element_count = linked_list.count(2)
print(f"\nCount of element 2: {element_count}\n")

# Display the elements of the linked list again
linked_list.display()
