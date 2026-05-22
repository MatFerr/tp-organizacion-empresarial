## tp-organizacion-empresarial
* **Institución:** Universidad Tecnológica Nacional (UTN)
* **Carrera:** Tecnicatura Universitaria en Programación (TUP) - Modalidad a Distancia
* **Cátedra:** Organización Empresarial
* **Año Lectivo:** 2026
* **Integrantes del Equipo:** Matías Ferreyra DNI:46452951 (Desarrollo Individual - Asumiendo Roles P1, P2 y P3)
* **Escenario B: Análisis de Ventas de una Pequeña Empresa** Este proyecto implementa un flujo de trabajo ágil y un script reproducible en Python para procesar registros de transacciones comerciales, calcular indicadores clave de rendimiento y exportar gráficos evolutivos de ingresos.

## El proyecto adopta la siguiente organización:
* /datos: Contiene el archivo fuente 'dataset.csv' con los registros simulados de las ventas.
* /scripts: Aloja el código principal 'analisis_datos.py' desarrollado en Python.
* /resultados: Carpeta automatizada donde se exporta el grafico 'grafico_ventas.png'.
* .gitignore: Configurado para excluir archivos temporales de Python.

##  Descripción del Dataset Utilizado
El archivo 'datos/dataset.csv' almacena una matriz de datos estructurada en base a las siguientes variables comerciales:
1. id: Identificador numérico único de la transacción.
2. producto: Nombre del artículo tecnológico comercializado (Teclado, Mouse, Monitor).
3. cantidad_vendida: Cantidad de unidades vendidas en la operación (entero).
4. precio: Valor unitario del producto en pesos (entero).
5. fecha_venta: Registro temporal de la transacción bajo formato internacional (YYYY-MM-DD).
