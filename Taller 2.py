#Taller 2, se debe completar el taller 1 xon:
#Dando continuidad con la primera entrega del proyecto, en esta oportunidad el estudiante debe realizar las siguientes validaciones utilizando la sentencia condicional IF.
#Si el empleado es mayor de 55 años disfrutará de un bono de prepensión correspondiente al 5% de su sueldo básico.
#Si el empleado es casado y tiene hijos se le otorgará un paseo cada diciembre
#Si el sueldo básico está entre 1000000 y 1500000 tendrá una comisión del 2% sobre el valor del sueldo; Si el sueldo básico está entre 1500001 y 2000000 tendrá una comisión del 5% sobre el valor del sueldo; para todos los demás casos no habrá comisión.
#Si el empleado trabajó más de 20 días al mes y su sueldo es menor a 1000000 tendrá derecho a un bono de alimentación.

print("Taller 2")
print(" ")
print("Por favor llene el siguiente formulario:")
print(" ")

UserName=input("Por favor digite su nombre: ")
UserLast=input("Por favor digite sus apellidos:  ")

validador=0
while validador==0: #ingreso # identificacion
    try:
        idenNum=int(input("\nPor favor digite su numero de identificacion: "))
        validador=1
    except ValueError:
        print("\nValor ingresado no valido")

UserAdr=input("\nPor favor digite su direccion: ")

validador=0
while validador==0:#ingreso # de telefono
        try:
            UserNum=int(input("\nPor favor digite su telefono: "))
            validador=1
        except ValueError:
            print("\nValor ingresado no valido")

validador=0
while validador==0:#ingreso edad
    try:
        UserAge=int(input("\nPor favor digite su edad: "))
        validador=1
    except ValueError:
        print("\nValor ingresado no valido")

validador= 0
while validador == 0 :#ingreso estado civil
    try:
        UserSta=int(input("\nPor favor seleccione su estado civil:\n1. Casado\n2. Soltero\n3. Union libre "))
        if UserSta<4 and UserSta>0:
            validador=1
        else:print("\nOpcion no valida")
    except ValueError:
        print("\nPor favor digite un numero")

validador=0

while validador==0:#ingreso # de hijos
    try:
        NumHij=int(input("\nPor favor digite su numero de hijos: "))
        NumHij=int(NumHij)
        validador=1
    except ValueError:
        print("\nValor ingresado no valido")    

validador=0
while validador==0:#ingreso estatura
    try:
        Estatura=int(input("\nPor favor digite su estatura en centimetros: "))
        validador=1
    except ValueError:
        print("\nValor ingresado no valido")

validador=0
while validador==0:#ingreso sueldo base
    try:        
        Sueldo=int(input("\nPor favor digite su sueldo basico: "))
        validador=1
    except ValueError:
        print("\nValor ingresado no valido")
        
validador=0
while validador==0:#ingreso dias laborados
    try:
        LabDia=int(input("\nPor favor digite el numero de dias laboradosen el mes: "))
        validador=1
    except ValueError:
        print("\nValor ingresado no valido")

if UserAge>=55:#Validacion prepension
    prepension=Sueldo*0.05
else:
    prepension="No tiene bono prepensión"

if UserSta==1 and NumHij>0:#validacion paseo
    paseo="Si, recuerde reclamar su paseo de fin de año"
else:
    paseo="No tiene derecho a paseo"

if Sueldo>=1000000 and Sueldo<=1500000:#validacion comision
    comision=Sueldo*0.02
elif Sueldo>1500000 and Sueldo<=2000000:
    comision=Sueldo*0.05
else:
    comision="No tiene comision"

if LabDia>20 and Sueldo<1000000:#validacion bono de alimentacion
    alimentacion="Tiene derecho a bono de alimentacion"
else:
    alimentacion="No tiene derecho a bono de alimentacion"

validador=0
validador0=0
print("\n_____SUELDO DEL MES______")
print(f"\nDATOS DEL TRABAJADOR: \nNOMBRE COMPLETO: {UserName} {UserLast} \nDIRECCION: {UserAdr} \nTELEFONO {UserNum}")
try:
    prepension=int(prepension)
    print(f"\nEmpleado tiene derecho a bono prepension?: si ${prepension:,.0f}") 
    validador=1
except:
    print(f"\nEmpleado tiene derecho a bono prepension?: {prepension}") 

print(f"\nEmpleado tiene derecho a paseo fin de año?: {paseo}")

try:
    comision=int(comision)
    print(f"\nEl empleado tiene comision?: Si ${comision:,.0f}")
    validador0=1
except:
    print(f"\nEl empleado tiene comision?: No tiene comision")

print(f"\nEmpleado tiene bono de alimentacion?: {alimentacion}")

if validador==1 and validador0==0:
    total=Sueldo+prepension
    print(f"\n TOTAL A PAGAR: ${total:,.0f}")
elif validador0==1 and validador==0:
    total=Sueldo+comision
    print(f"\n TOTAL A PAGAR: ${total:,.0f}")
elif validador==1 and validador0==1: 
    total=Sueldo+comision+prepension
    print(f"\n TOTAL A PAGAR: ${total:,.0f}")
else:
    print(f"\n TOTAL A PAGAR: ${Sueldo:,.0f}")
