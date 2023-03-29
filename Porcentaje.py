#Un maestro desea saber qué porcentaje de hombres y que
#porcentaje de mujeres hay en un grupo de estudiantes.

print("\nPorcentaje de estudiantes mujeres VS hombres\n")
hombres=int(input("Por favor ingrese la cantidad de hombres del curso: "))
mujeres=int(input("Por favor ingrese la cantidad de mujeres del curso: "))
curso=hombres+mujeres
Phombres=(hombres/curso)*100
Pmujeres=100-Phombres
print(f'\n\nEl total de estudiantes es {curso:,.0f}\n\n{Phombres:,.0f}% son hombres y {Pmujeres:,.0f}% son mujeres ')