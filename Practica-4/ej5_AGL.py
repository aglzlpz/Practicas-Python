num=int(input("Escribe un número: "))
primo=True
for i in range(2,num):
    if(num%i==0):
        primo=False
        break

if(primo):
    print(f"El número {num} es primo")
else: 
    print(f"El número {num} no es primo")