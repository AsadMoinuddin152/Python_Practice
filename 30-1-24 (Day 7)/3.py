class Node:
    def __init__(self, data):
        # Initialize a node with data and a reference to the next node
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        # Initialize an empty queue with head and tail set to None
        self.head = None
        self.tail = None

    def is_empty(self):
        # Check if the queue is empty
        return self.head is None

    def enqueue(self, data):
        # Add a new node with the given data to the end of the queue
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        # Remove and return the front element of the queue
        if self.is_empty():
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return data
    
    def display(self):
        # Display the elements of the queue
        if self.is_empty():
            print("Queue is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end="")
                if current.next:
                    print("-->", end="")
                current = current.next
            print()

# Create a Queue instance
queue = Queue()

# Enqueue elements into the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

# Display the elements of the queue
queue.display()

# Dequeue an element from the queue
print("Dequeued element:", queue.dequeue())

# Display the elements of the updated queue
queue.display()
