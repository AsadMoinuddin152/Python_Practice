def checkNonPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return num
    return 0

number = int(input())
total = 0
while number > 0:
    temp = number % 10
    total += checkNonPrime(temp)
    number = number // 10
print(total)