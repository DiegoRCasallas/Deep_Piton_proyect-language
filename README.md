# DeepPiton: Lenguaje de Dominio Específico para Deep Learning

DeepPiton es un DSL (Domain Specific Language) diseñado para facilitar la definición, entrenamiento y evaluación de modelos de Deep Learning y Machine Learning. Construido sobre Python utilizando ANTLRv4, ofrece una sintaxis familiar y sencilla, permitiendo a los usuarios centrarse en la lógica de sus modelos sin la complejidad de las librerías tradicionales.

> **Nota:** Este proyecto implementa todas las operaciones matemáticas y de Deep Learning desde cero, sin dependencias externas como NumPy o TensorFlow, para fines educativos y de demostración.

## Tabla de Contenidos
1. [Uso](#uso)
2. [Sintaxis Básica](#sintaxis-básica)
3. [Operaciones Matemáticas y Matriciales](#operaciones-matemáticas-y-matriciales)
4. [Estructuras de Control](#estructuras-de-control)
5. [Funciones](#funciones)
6. [Deep Learning API](#deep-learning-api)
7. [Visualización](#visualización)
8. [Ejemplos](#ejemplos)

## Uso

Para ejecutar un script de DeepPiton (`.dp`), utiliza el intérprete desde la línea de comandos:

```bash
python deep_piton.py ruta/al/archivo.dp
```

## Sintaxis Básica

### Variables y Tipos de Datos
DeepPiton soporta números (enteros y flotantes), cadenas de texto y listas (que pueden representar vectores o matrices).

```python
x = 10
y = 3.14
nombre = "DeepPiton"
lista = [1, 2, 3]
matriz = [[1, 0], [0, 1]]
```

## Operaciones Matemáticas y Matriciales

Soporta operaciones aritméticas estándar y operaciones específicas para álgebra lineal.

| Operación | Sintaxis | Descripción |
|-----------|----------|-------------|
| Suma | `a + b` | Suma de escalares o matrices. |
| Resta | `a - b` | Resta de escalares o matrices. |
| Multiplicación | `a * b` | Multiplicación escalar o elemento a elemento. |
| División | `a / b` | División escalar. |
| Potencia | `a ** b` | Potencia. |
| Producto Matricial | `A @ B` o `MM(A, B)` | Multiplicación de matrices. |
| Transpuesta | `TRP(A)` | Transpuesta de una matriz. |
| Inversa | `INV(A)` | Inversa de una matriz. |

## Estructuras de Control

Sintaxis similar a Python para el control de flujo.

### If / Elif / Else
```python
if x > 0:
    print("Positivo")
elif x < 0:
    print("Negativo")
else:
    print("Cero")
```

### While
```python
i = 0
while i < 5:
    print(i)
    i = i + 1
```

### For
```python
for x in [1, 2, 3]:
    print(x)
```

## Funciones

Definición de funciones personalizadas.

```python
def cuadrado(n):
    return n * n

resultado = cuadrado(5)
```

## Deep Learning API

Funciones integradas para construir y entrenar modelos.

### Manejo de Datos
- **`CARGAR_CSV("ruta.csv")`**: Carga un archivo CSV como una matriz.
- **`GUARDAR_TEXTO("ruta.txt", datos)`**: Guarda datos en un archivo de texto.

### Creación de Modelos
- **`MODELO()`**: Crea una instancia de un modelo de red neuronal vacío.
- **`REGRESION_LINEAL()`**: Crea un modelo específico para regresión lineal.

### Capas
- **`CAPA_DENSA(entradas, salidas, activacion)`**: Define una capa densa.
    - `activacion`: Puede ser `"relu"`, `"sigmoid"`, `"tanh"`, o `None`.

### Entrenamiento
- **`ENTRENAR(modelo, X, Y, epocas, learning_rate)`**: Entrena un modelo de red neuronal.
- **`AJUSTAR(modelo, X, Y)`**: Entrena un modelo de regresión lineal (usa la ecuación normal o descenso de gradiente interno).

### Predicción
- **`modelo.adelante(X)`**: Realiza una pasada hacia adelante (inferencia) en una red neuronal.
- **`modelo.predecir(X)`**: Realiza una predicción con un modelo de regresión.

## Visualización

- **`GRAFICAR_DISPERSION(X, Y, [Predicciones])`**: Genera un gráfico de dispersión en arte ASCII en la consola.

## Ejemplos

### 1. Operaciones Básicas
```python
m1 = [[1, 2], [3, 4]]
m2 = [[1, 0], [0, 1]]
producto = m1 @ m2
print(producto)
```

### 2. Red Neuronal (XOR)
Este ejemplo entrena una red neuronal simple para resolver el problema XOR.

```python
# Datos XOR
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [[0], [1], [1], [0]]

# Definir Modelo
m = MODELO()
m.agregar(CAPA_DENSA(2, 4, "relu"))    # Capa oculta: 2 entradas, 4 neuronas
m.agregar(CAPA_DENSA(4, 1, "sigmoid")) # Capa salida: 4 entradas, 1 neurona

# Entrenar
print("Entrenando...")
ENTRENAR(m, X, Y, 1000, 0.1)

# Predecir
pred = m.adelante(X)
print("Predicciones:")
print(pred)

# Visualizar
GRAFICAR_DISPERSION(X, pred)
```