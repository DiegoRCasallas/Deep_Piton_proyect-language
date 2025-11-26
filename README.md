Título: Diseño e Implementación del Lenguaje de Dominio Específico DeepPiton para Aprendizaje Profundo.

Objetivo: Desarrollar un DSL llamado DeepPiton utilizando ANTLRv4 y el patrón Visitor en Python. DeepPiton ofrecerá una sintaxis simple y familiar, similar a Python, para definir, entrenar y evaluar modelos de Deep Learning (DL) y Machine Learning (ML).

🎯 Condición Fundamental (El Desafío Central):
Queda estrictamente prohibido el uso de librerías externas para operaciones matemáticas, de álgebra lineal o de Deep Learning (ej. NumPy, SciPy, Pandas, TensorFlow, PyTorch). Todas las estructuras y algoritmos (manejo de matrices, multiplicación, activación, loss functions, optimizadores) deben ser implementados desde cero en Python, utilizando estructuras de datos nativas (listas, diccionarios, etc.) como backend de ejecución del DSL.

1. Requisitos de Sintaxis y Semántica (Gramática ANTLR)
DeepPiton debe soportar una sintaxis tipo Python para:

Variables y Asignación: variable = expresion

Operaciones Aritméticas: +, -, *, /, %, Potencia (**).

Operaciones Matriciales: Sintaxis para la Multiplicación Matricial (ej. A @ B o MM(A, B)), Transpuesta (TRP(A)) e Inversa (INV(A)).

Estructuras de Control: if/elif/else, for y while.

Definición de Funciones: def nombre_funcion(parametros):

2. Módulos de Aprendizaje Profundo (Implementación en el Visitor)
El lenguaje debe incluir funciones embebidas (built-in) que se mapeen a tu lógica Python implementada desde cero:

Manejo de Datos:

CARGAR_CSV("ruta.csv"): Carga datos a una estructura de matriz de DeepPiton.

GUARDAR_TEXTO("ruta.txt", datos).

Modelado DL/ML:

def modelo_MLP(): (Sintaxis Python-like para definir la arquitectura).

CAPA_DENSA(entradas, salidas, activacion='relu'): Función para añadir una capa a un modelo.

ENTRENAR(modelo, datos, etiquetas, epocas, lr): Llama a tu algoritmo de backpropagation nativo.

Funciones de ML predefinidas: regresion_lineal(X, Y), clasificador_perceptron(X, Y).

3. Ejecución y Visualización (Arte ASCII)
El intérprete se ejecutará desde la consola, recibiendo un archivo fuente (e.g., python deep_piton.py mi_codigo.dp).

Los resultados y errores se mostrarán en la consola.

Gráficos (Arte ASCII): El lenguaje debe incluir una función nativa para visualización que represente los datos y/o el progreso del entrenamiento utilizando exclusivamente caracteres de texto (Arte ASCII), asegurando que no se requieran librerías de interfaz gráfica.

Ejemplo de función: GRAFICAR_DISPERSION(X, Y) que imprime un gráfico de dispersión en texto.