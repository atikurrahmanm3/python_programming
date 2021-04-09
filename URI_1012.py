a, b, c = input().split(" ")
pi = 3.14159
triangle = (float(a) * float(c))/2
circle = pi * float(c)**2
trapezium = float(c) * ((float(a) + float(b))/2)
square = float(b) ** 2
rectangle = float(a) * float(b)
print("TRIANGULO: %.3f" % triangle)
print("CIRCULO: %.3f" % circle)
print("TRAPEZIO: %.3f" % trapezium)
print("QUADRADO: %.3f" % square)
print("RETANGULO: %.3f" % rectangle)
