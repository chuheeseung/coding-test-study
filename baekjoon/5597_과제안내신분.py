students = [0 for _ in range(30)]
submitted = []

for _ in range(28):
    n = int(input())
    students[n-1] = 1

print(students.index(0) + 1)
students[students.index(0)] = 1
print(students.index(0) + 1)