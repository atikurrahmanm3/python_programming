# a = [6, 9, 20, 4]
# print(sum(a))
a = []
for i in range(4):
    n = int(input(f"Enter numbers {i}: "))
    a.append(n)
print(f"The numbers of a list is: {a}")
s = 0
for i in a:
    s += i

print(f"The sum of The List is: {s}")
