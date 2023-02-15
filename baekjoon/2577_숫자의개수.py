a, b, c = int(input()), int(input()), int(input())
multiple = a * b * c

numbers = list(str(multiple))
for i in range(10):
    print(numbers.count(str(i)))
