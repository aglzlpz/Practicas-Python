edad=int(input("¿Cuántos años tiene el contribuyente?"))
ingresos=float(input("¿Cuántos son sus ingresos mensuales?"))
if(edad<16 or ingresos<1000):
    print("No tiene que tributar")
else:
    print("Tiene que tributar")