from src.math_core import Matriz

def cargar_csv(ruta_archivo):
    datos = []
    try:
        with open(ruta_archivo, 'r') as f:
            lineas = f.readlines()
            for linea in lineas:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(',')
                try:
                    fila_flotante = [float(x.strip()) for x in partes]
                    datos.append(fila_flotante)
                except ValueError:
                    continue # Saltar encabezado o filas no numéricas
        return Matriz(datos)
    except FileNotFoundError:
        print(f"Error: Archivo {ruta_archivo} no encontrado.")
        return Matriz([])

def guardar_texto(ruta_archivo, datos):
    with open(ruta_archivo, 'w') as f:
        f.write(str(datos))

def graficar_dispersion_ascii(matriz_x, matriz_y, matriz_pred=None, ancho=60, alto=20):
    """
    Dibuja un gráfico de dispersión ASCII.
    matriz_x: Matriz (Nx1)
    matriz_y: Matriz (Nx1)
    matriz_pred: Matriz (Nx1) opcional (predicciones)
    """
    if matriz_x.filas != matriz_y.filas:
        print("Error: X e Y deben tener el mismo número de filas")
        return

    xs = [fila[0] for fila in matriz_x.datos]
    ys = [fila[0] for fila in matriz_y.datos]
    
    preds = []
    if matriz_pred:
        if matriz_pred.filas != matriz_x.filas:
             print("Error: Predicciones deben tener el mismo número de filas que X")
             return
        preds = [fila[0] for fila in matriz_pred.datos]

    if not xs or not ys:
        print("No hay datos para graficar")
        return

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    if preds:
        min_y = min(min_y, min(preds))
        max_y = max(max_y, max(preds))
    
    rango_x = max_x - min_x if max_x != min_x else 1
    rango_y = max_y - min_y if max_y != min_y else 1

    cuadricula = [[' ' for _ in range(ancho)] for _ in range(alto)]

    # Dibujar puntos de datos
    for x, y in zip(xs, ys):
        col = int((x - min_x) / rango_x * (ancho - 1))
        fila = int((y - min_y) / rango_y * (alto - 1))
        fila = alto - 1 - fila
        if 0 <= fila < alto and 0 <= col < ancho:
            cuadricula[fila][col] = '*'
            
    # Dibujar predicciones (línea)
    if preds:
        for x, y in zip(xs, preds):
            col = int((x - min_x) / rango_x * (ancho - 1))
            fila = int((y - min_y) / rango_y * (alto - 1))
            fila = alto - 1 - fila
            if 0 <= fila < alto and 0 <= col < ancho:
                if cuadricula[fila][col] == ' ':
                    cuadricula[fila][col] = '.'
                else:
                    cuadricula[fila][col] = '+' # Superposición

    # Dibujar eje y y cuadrícula
    print(f"{max_y:.2f}")
    for i, fila in enumerate(cuadricula):
        linea = "".join(fila)
        if i == alto // 2:
            print(f"| {linea} ")
        else:
            print(f"| {linea}")
    print(f"{min_y:.2f}")
    print(" " + "-" * ancho)
    print(f"{min_x:.2f}".ljust(ancho // 2) + f"{max_x:.2f}".rjust(ancho // 2))
