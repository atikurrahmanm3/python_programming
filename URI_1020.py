days = int(input())
M = (days / 30) % 12
Y = days/365
D = days % 365
day = D % 30

print("%d ano(s)" % Y)
print("%d mes(es)" % M)
print("%d dia(s)" % day)
# print(year, "ano(s)")
# print(month, "mes(es)")
# print(day, "dia(s)")
