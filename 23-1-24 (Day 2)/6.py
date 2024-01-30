# Define the SuperList class, inheriting from the built-in list class
class SuperList(list):
    def __len__(self):
        return 1000

# Create an instance of the SuperList class
super_list1 = SuperList()

# Print the custom length of the SuperList
print(len(super_list1))

# Append an element to the SuperList
super_list1.append(5)

# Print the first element of the SuperList
print(super_list1[0])

# Print the custom length of the SuperList after appending an element
print(len(super_list1))

# Uncomment the following line to check if SuperList is a subclass of list
# print(issubclass(SuperList, list))
