year=int(input("Escribe un año: "))

if(year%4==0):
    
    if(year%100==0):

        if(year%400==0):
            
            print("Es un año bisiesto")

        else:print("No es un año bisiesto")

    else:print("Es un año bisiesto")

else:print("No es un año bisiesto")