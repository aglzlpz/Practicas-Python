frase=str(input("Escribe una frase: "))

#FORMA LARGA
invertida1=str()
i=-1
while(i>=-len(frase)):
    invertida1+=frase[i]
    i-=1

#FORMA FÁCIL
invertida2=frase[::-1]

print(f"Usando la forma compleja: {invertida1}")
print(f"Usando la forma simple: {invertida2}")