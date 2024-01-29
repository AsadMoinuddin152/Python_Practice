string = input()
n_string = len(string)
l_string = ''
for i in range(0, n_string):
    if i % 2 == 0:
        l_string += string[i]
print(l_string)