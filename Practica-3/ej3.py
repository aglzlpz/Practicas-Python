dividendo=float(input("Introduce el dividendo de la división: "))
divisor=float(input("Introduce el divisor de la división: "))
if(divisor==0):
    print("ERROR: El divisor no puede ser 0")
else:
    print(f"El resultado de la división es {dividendo/divisor}")