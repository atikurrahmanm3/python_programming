a, b, c = input().split()
maior = int((int(a) + int(b) + abs(int(a) - int(b)))/2)
result = int((maior + int(c) + abs(maior - int(c)))/2)
print(result, "eh o maior")
