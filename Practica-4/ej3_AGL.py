c1=float(input("Introduce la longitud de un cateto: "))
c2=float(input("Introduce la longitud de un cateto: "))
if(c1<=0 or c2<=0):
    print("ERROR")
    quit()

h=(c1**2+c2**2)**(1/2)
print("La hipotenusa es ",h)