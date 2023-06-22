libros = 5
precio_libro = 30.50
lapices = 6
precio_lapiz = 5.60
plumas = 3
precio_pluma = 6.20
hojas = 1000
precio_hoja = 105.00

total_libros = libros * precio_libro
total_lapices = lapices * precio_lapiz
total_plumas = plumas * precio_pluma
total_hojas = hojas * (precio_hoja / 1000)

monto_total = total_libros + total_lapices + total_plumas + total_hojas

print("Rebeca pagó en total:", monto_total, "euros")
