import os
import matplotlib.pyplot as plt

ruta_csv = os.path.join('datos', 'archivo.csv')
ruta_grafico = os.path.join('resultados', 'grafico_ventas.png')

datos = []
with open(ruta_csv, mode="r" ) as f:
  lineas = f.readlines()
  for linea in lineas[1:]:
      dato = linea.strip().split(",")
      datos.append(dato)

ventas_totales = 0
cantidades_por_producto = {}
ventas_por_mes = {}
for dato in datos:
  mes = dato[4][0:7]
  ventas_totales += (int(dato[2]) * int(dato[3]))

  if(dato[1] in cantidades_por_producto):
    cantidades_por_producto[dato[1]] += int(dato[2])
  else:
      cantidades_por_producto[dato[1]] = int(dato[2])
  if(mes in ventas_por_mes):
    ventas_por_mes[mes] += int(dato[2])
  else:
    ventas_por_mes[mes] = int(dato[2])

producto_mas_vendido = max(cantidades_por_producto, key=cantidades_por_producto.get)

print(f"Ventas Totales: ${ventas_totales}")
print(f"Producto más vendido: {producto_mas_vendido}")

meses_ordenados = sorted(list(ventas_por_mes.keys()))
montos_ordenados = []
for mes in meses_ordenados:
    montos_ordenados.append(ventas_por_mes[mes])

plt.figure(figsize=(6, 3))
plt.bar(meses_ordenados, montos_ordenados, color='skyblue')
plt.title('Evolución de Ventas')
plt.ylabel('Monto ($)')
plt.tight_layout()


os.makedirs('resultados', exist_ok=True)
plt.savefig(ruta_grafico)
print("Gráfico guardado con éxito.")
