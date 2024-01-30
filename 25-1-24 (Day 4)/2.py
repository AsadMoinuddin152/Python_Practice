def bubble_sort(num):
    """
    Perform bubble sort on a list of numbers.

    Parameters:
    - num (list): List of numbers to be sorted.

    Returns:
    - list: Sorted list in ascending order.
    """
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

# Example usage
num = [5, 2, 1, 3, 4]
print(bubble_sort(num))
