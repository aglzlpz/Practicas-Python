numeros=[1,2,3,4,5,6,7,8,9]
numsuma=[numeros[0]]
for i in range (1,len(numeros)):
    numsuma.append(numsuma[i-1]+numeros[i])

print(f"La suma de los números de la lista es {numsuma}")
