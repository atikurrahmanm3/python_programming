# n = float(input())
# print(n)
# l = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
#
# for i in l:
#     print(f"{n // i} nota(s) de R$  {i},00")
#     n = n % i
#     i += 1


# n = float(input())
# print("NOTAS:")
# print(n//100, "nota(s) de R$ 100.00")
# n = n % 100
# print(n//50, "nota(s) de R$ 50.00")
# n = n % 50
# print(n//20, "nota(s) de R$ 20.00")
# n = n % 20
# print(n//10, "nota(s) de R$ 10.00")
# n = n % 10
# print(n//5, "nota(s) de R$ 5.00")
# n = n % 5
# print(n//2, "nota(s) de R$ 2.00")
# n = n % 2
# print("MOEDAS:")
# print(n//1, "moeda(s) de R$ 1.00")
# n = n % 1
# print(n//0.50, "moeda(s) de R$ 0.50")
# n = n % 0.50
# print(n//0.25, "moeda(s) de R$ 0.25")
# n = n % 0.25
# print(n//0.10, "moeda(s) de R$ 0.10")
# n = n % 0.10
# print(n//0.05, "moeda(s) de R$ 0.05")
# n = n % 0.05
# print(n//0.01, "moeda(s) de R$ 0.01")
# n = n % 0.01


A=float(input())
N=A
a=N/100
b=N%100
c=b/50
d=b%50
e=d/20
f=d%20
g=f/10
h=f%10
i=h/5
j=h%5
k=j/2
l=j%2

E=A*100
B=(int(E))
m=B%100
n=m/50
o=m%50
p=o/25
q=o%25
r=q/10
s=q%10
t=s/5
u=s%5
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(a)))
print("{} nota(s) de R$ 50.00".format(int(c)))
print("{} nota(s) de R$ 20.00".format(int(e)))
print("{} nota(s) de R$ 10.00".format(int(g)))
print("{} nota(s) de R$ 5.00".format(int(i)))
print("{} nota(s) de R$ 2.00".format(int(k)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(l)))
print("{} moeda(s) de R$ 0.50".format(int(n)))
print("{} moeda(s) de R$ 0.25".format(int(p)))
print("{} moeda(s) de R$ 0.10".format(int(r)))
print("{} moeda(s) de R$ 0.05".format(int(t)))
print("{} moeda(s) de R$ 0.01".format(int(u)))