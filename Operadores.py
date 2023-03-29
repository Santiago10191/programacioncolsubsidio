#Se recibe una venta de un producto aplicar el 19% de IVA y conocer el total
venta=float(input("Cuánto fue el total de la compra?"))
iva=venta*0.19
total=iva+venta
print("El iva es ${:,.0f} y el total a pagar es ${:,.0f}".format(iva,total))
print(f"El iva es ${iva:,.0f} y el total a pagar es ${total:,.0f}")