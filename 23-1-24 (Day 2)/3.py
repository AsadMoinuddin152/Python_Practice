# Get input sets for three subjects
sub1 = set(map(int, input().split()))
sub2 = set(map(int, input().split()))
sub3 = set(map(int, input().split()))

# Find the common elements among the three subjects
common = (sub1.intersection(sub2)).intersection(sub3)

# Convert the common elements to a list and sort it
common = list(common)
common.sort()

# Print the sorted list of common elements
print(common)
