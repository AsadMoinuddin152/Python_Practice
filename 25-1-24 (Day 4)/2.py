def bubble_sort(num):
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

num = [5, 2, 1, 3, 4]
print(bubble_sort(num))
