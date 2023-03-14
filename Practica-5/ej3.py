asig=["ART","Propagación","Esgrima","Python"]
notas=[]
for i in range (len(asig)):
    nota=int(input(f"¿Qué has sacado en {asig[i]}?"))
    notas.append(nota)

for i in range (len(asig)):
    print(f"{asig[i]}: {notas[i]}")