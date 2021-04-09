x = int(input())
y = int(input())

if x > y:
    a = y
    b = x
if x <= y:
    a = x
    b = y

total = 0

while a <= b:
    if a % 13 != 0:
        total = total + a
    a = a + 1
print(total)
