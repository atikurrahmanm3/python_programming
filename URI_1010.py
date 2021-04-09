# c1, u1, p1 = input().split(" ")
# c2, u2, p2 = input().split(" ")
#
# total = (int(u1) * float(p1)) + (int(u2) * float(p2))
#
# print("VALOR A PAGAR = R$ %.2f" %total)
#

c1, u1, p1 = input().split(" ")
c2, u2, p2 = input().split(" ")
product1 = int(u1) * float(p1)
product2 = int(u2) * float(p2)
total = float(product1 + product2)
print("VALOR A PAGAR: R$ %.2f" %total)
