asig=["ART","Propagación","Esgrima","Python"]
aprobadas=[]
for i in range (len(asig)):
    nota=int(input(f"¿Qué has sacado en {asig[i]}?"))
    if nota>=5:
        aprobadas.append(asig[i])

for i in range (len(aprobadas)):
    asig.remove(aprobadas[i])

print(f"Las asignaturas suspensas son {asig}")
print(f"Las asignaturas aprobadas son {aprobadas}")