veggie=["pimiento","tofu"]
noveggie=["pepperoni","jamón","salmón"]

veg=input("¿Quieres una pizza vegetariana? 'S' para sí y 'N' para no: ")
veg=veg.lower()
if(veg=="s"):      #VEGETARIANO
    print("Los ingredientes vegetarianos disponibles son: ")
    for ing in veggie:      #LISTA INGREDIENTES
        print(ing)
    selec=input(f"Escribe el ingrediente vegetariano deseado: ").lower()
    if(selec!="pimiento" and selec !="tofu"):
        print("Has elegido un ingrediente que no existe")
    else:
        print(f"Has elegido la pizza vegetariana de tomate, mozzarella y {selec}")

else:   #NO VEGETARIANO
    print("Los ingredientes no vegetarianos disponibles son: ")
    for ing in noveggie:    #LISTA INGREDIENTES
        print(ing)
    
    selec=input(f"Escribe el ingrediente no vegetariano deseado: ").lower()
    if(selec!="pepperoni" and selec!="jamón" and selec!="salmón"):
        print("Has elegido un ingrediente que no existe")
    else:
        print(f"Has elegido la pizza no vegetariana de tomate, mozzarella y {selec}")    