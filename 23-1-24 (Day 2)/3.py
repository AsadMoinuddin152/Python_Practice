sub1 = set(map(int, input().split()))
sub2 = set(map(int, input().split()))
sub3 = set(map(int, input().split()))
common = (sub1.intersection(sub2)).intersection(sub3)
common = list(common)
common.sort()
print(common)