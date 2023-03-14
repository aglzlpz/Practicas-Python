nombre=str(input("Dime tu nombre:"))
num=int(input("Dime un número: "))

#BUCLE
print("Usando un bucle: ")
i=0
while(i<num):
    print(nombre)
    i+=1

#CONCATENANDO
print("Concatenando: ")
nombreconc=nombre+"\n"
print(nombreconc*num)