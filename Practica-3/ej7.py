edad=int(input("¿Cuántos años tienes?"))
aprob=str(input("¿Has aprobado Python? Escribe 'S' para sí y 'N' para no. "))
if(aprob=="S"):
    aprobado=True
else:
    aprobado=False

if(edad<18):
    print("No hay entradas para menores de edad")
elif(edad>=30 or aprobado):
    print("Entrada gratis")
elif(edad>=18 and edad<=25):
    print("Entrada a 5€")
else:
    print("Entrada a 15€")