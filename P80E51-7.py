peso_vagon_vacio = 6425.0
peso_contenedor = 845.75
peso_cilindro = 650.8

cantidad_contenedores = 3
cantidad_cilindros = 2

peso_total_cargado = peso_vagon_vacio + \
    (cantidad_contenedores * peso_contenedor) + \
    (cantidad_cilindros * peso_cilindro)

print("El peso del vagón ya cargado es:", peso_total_cargado, "kilogramos")
