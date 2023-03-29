# Taller 1 
# No de Identificación, Nombres, Apellidos, Dirección, Teléfono, Edad, Estado Civil, 
# Número de hijos, Estatura en centímetros, fecha de contratación (Día/mes/año), Sueldo básico, Días Laborados

print("Taller 1");
print(" ")
print("Por favor llene el siguiente formulario:")
print(" ")
UserName=input("Por favor digite su nombre: ")
UserLast=input("Por favor digite sus apellidos:  ")
idenNum=input("Por favor digite su numero de identificacion: ")
UserAdr=input("Por favor digite su direccion: ")
UserNum=input("Por favor digite su telefono: ")
UserAge=input("Por favor digite su edad: ")
UserSta=input("Por favor digite su estado civil: ")
NumHij=input("Por favor digite su numero de hijos: ")
Estatura=input("Por favor digite su estatura en centimetros: ")
FechaCon=input("Por favor digite su fecha de contratacion (Dia/Mes/año): ")
Sueldo=input("Por favor digite su sueldo basico: ")
LabDia=input("Por favor digite el numero de dias laborados: ")
#Finaliza captura de datos
print(" ")
print(f"A continuación podrá ver los datos ingresados: \n Su nombre es: {UserName} {UserLast}  tiene {UserAge} años, y mide {Estatura}cms")
print("Su numero de identificacion es: ", idenNum)
print("Su direccion es: ", UserAdr)
print("Su numero de telefono es: ",UserNum)
print("Su estado civil es: ",UserSta)
print("Usted tiene ",NumHij," hijos")
print("Usted fue contratado ",FechaCon, "con sueldo basico de ",Sueldo," pesos y ha laborado ",LabDia, " dias")



