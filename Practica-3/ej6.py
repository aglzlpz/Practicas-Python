#grupo A --> Mujeres(A-L) y Hombres(Ñ-Z)
#grupo B --> Mujeres(M-Z) y hombres(A-N)
nombre=input("¿Cuál es tu nombre?").upper()
sexo=input("¿Eres hombre o mujer? (Escribe 'H' si eres Hombre y 'M' si eres mujer)").upper()
if((nombre[0]<="M" and sexo=="M") or (nombre[0]>="N" and sexo=="H")):
    print("Grupo A")
else:
    print("Grupo B")