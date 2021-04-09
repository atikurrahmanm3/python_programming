num = int(input("How many numbers? "))
total = 0
for n in range(num):
    marks = float(input("Enter number: "))
    total += marks

print(f"Total marks is: {total}")
avg = total/num
print(f"The avarege is : {avg}")
