#input
a = int(input("Ingrese el primer numero entero:"))
b = int(input("Ingrese el segundo numero entero:"))
c = int(input("Ingrese el tercer numero entero:"))

#Process

if a>b:
    if a>c:
        mayor = a
    else:
        mayor = c
else:
    if b>c:
        mayor = b
    else:
        mayor = c

print("EL numero mayor es:", mayor)
