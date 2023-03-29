#Un vendedor recibe un sueldo base más un 10% extra por
#comisión de sus ventas, el vendedor desea saber cuánto
#dinero obtendrá por concepto de comisiones por las tres
#ventas que realiza en el mes y el total que recibirá en
#el mes tomando en cuenta su sueldo base y comisiones.

print("\n Calculadora de comisiones\n")
base=float(input("Por favor indique su salario base: "))
print("\nPor favor indique el valor de sus tres ventas: ")
ven1=float(input("venta 1: "))
ven2=float(input("venta 2: "))
ven3=float(input("venta 3: "))
conVen=(ven1+ven2+ven3)*0.1
total=conVen+base
print(f"\nEl valor de su comision es ${conVen:,.0f} y el total de su sueldo es ${total:,.0f}")