precio=str(input("Escribe el precio de un producto con dos decimales y usando un punto para separar euros y céntimos: "))
posicionpt=precio.find(".")
euros=precio[:posicionpt]
centimos=precio[posicionpt+1:]
if(len(centimos)!=2):
    print("Escribe el precio con dos decimales")
    quit()
print(f"{euros} euros y {centimos} céntimos")