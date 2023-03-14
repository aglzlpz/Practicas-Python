personas=[("Francisco",50), ("Ramón",44), ("Llanos",16), ("Paula",25)]
mayor=-1

for i in range (len(personas)):
    if(personas[i][1]>mayor):
        mayor=personas[i][1]
        imayor=i

menor=10000
for i in range (len(personas)):
    if(personas[i][1]<menor):
        menor=personas[i][1]
        imenor=i

print(f"El más viejo es {personas[imayor][0]} con {personas[imayor][1]} años")
print(f"El más joven es {personas[imenor][0]} con {personas[imenor][1]} años")
