frase=str(input("Escribe una frase: "))
letra=str(input("Escribe una vocal que quieras poner en mayúscula: "))
letraminusc=letra.lower()
if(letraminusc!="a" and letraminusc!="e" and letraminusc!="i" and letraminusc!="o" and letraminusc!="u"):
    print("¡Te he pedido una vocal!")
    quit()

newfrase=frase.replace(letraminusc,letra.capitalize())
print(newfrase)