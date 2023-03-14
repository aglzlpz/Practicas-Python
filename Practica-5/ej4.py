
loteria=[]
num=(input("Escriba los números ganadores de la lotería. Si ha escrito todos, escriba 'fin'."))
while (num!="fin"):
    if(int(num)>99 or int(num)<0):
        print("Escribe números del 0 al 99")
        break

    else:
        loteria.append(num)
        num=(input("Escriba los números ganadores de la lotería. Si ha escrito todos, escriba 'fin'."))

ordenados=sorted(loteria)
print(f"Los números de la lotería son {ordenados}")      
