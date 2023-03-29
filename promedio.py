#Un alumno desea saber cuál será su calificación final en
#la materia de Algoritmos. Dicha calificación se compone
#de tres exámenes parciales.

print("\n Calculadora de nota definitiva materia algoritmos\n")
cal1=float(input("Digite la calificacion del examen 1: "))
cal2=float(input("Digite la calificacion del exmane 2: "))
cal3=float(input("Digite la calificacion del examen 3: "))
promedio=round((cal1+cal2+cal3)/3,2)
print(f"\nSu nota final es {promedio}")



