costo_total_con_impuestos = 2541.50
impuestos_por_juguete = 0.15
cantidad_juguetes = 50

impuestos_totales = impuestos_por_juguete * cantidad_juguetes
costo_por_juguete = (costo_total_con_impuestos -
                     impuestos_totales) / cantidad_juguetes

print("El costo de cada juguete es:", costo_por_juguete, "euros")
