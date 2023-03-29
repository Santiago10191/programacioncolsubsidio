#Una tienda ofrece un descuento del 15% sobre el total
#de la compra y un cliente desea saber cuánto deberá
#pagar finalmente por su compra.

print("\n Descuento del 15%")
valor=float(input("\nPor favor ingrese el total de la compra: "))
descuento=valor*0.15
total=valor-descuento
print(f"\nEl total de su compra es ${total:,.0f} \n\nSu ahorro fue de ${descuento:,.0f}")