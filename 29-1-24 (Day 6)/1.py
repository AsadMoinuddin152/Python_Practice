class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def display(self):
        current = self.head
        print("Display of Elements :")
        while current:
            print(current.data, end="")
            if current.next:
                print("-->", end="")
            current = current.next
        print()

    def count(self, element):
        count = 0
        current = self.head
        while current:
            if current.data == element:
                count += 1
            current = current.next
        return count


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(0)
linked_list.append(2)
linked_list.append(3)
linked_list.display()

element_count = linked_list.count(2)
print(f"\nCount of element 2: {element_count}\n" )

linked_list.display()
