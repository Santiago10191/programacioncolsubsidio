#contador al 100
print("\Los numeros pares del 1 a al 100 son: ")
for i in range(0,101,2):
    print(i, end=" ")

#Tabla de multiplicar
validador=0
while validador==0:
    try:
        num=int(input("\n\nPor favor ingrese un numero para obtener la tabla de multiplicar del 0 al 10: "))
        num=int(num)
        validador=1
        for i in range(11):
            print(i,"x",num,"=",i*num)
    except ValueError:
        print("\nValor ingresado no valido")

#años que ha cumplido
validador=0
while validador==0:
    try:
        edad=int(input("\n\nPor favor ingrese su edad: "))
        edad=int(edad)
        validador=1
        for i in range(1,edad+1):
            print(i)
    except ValueError:
        print("\nValor ingresado no valido")

#numero entero positivo, muestre impares
validador=0
while validador==0:
    try:
        num1=int(input("\n\nIngrese un numero entero positivo: "))
        num1=int(num1)
        if num1<0:
            validador=0
        else:
            validador=1
    except ValueError:
        print("valor ingresado no es numero")
for i in range(1,num1+1,2):
    print(i, end=",")

#suma de numeros pares hasta el 100
acu=0
for i in range (0,101,2):
    acu=acu+i
print(f"\n\nEl total de la suma de los numeros hasta el 100 es: {acu}")