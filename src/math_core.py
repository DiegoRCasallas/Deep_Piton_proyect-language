

class AleatorioSimple:
    def __init__(self, semilla=12345):
        self.estado = semilla
        # Parámetros LCG (usando valores de glibc)
        self.a = 1103515245
        self.c = 12345
        self.m = 2**31

    def aleatorio(self):
        """Devuelve un flotante entre 0.0 y 1.0"""
        self.estado = (self.a * self.estado + self.c) % self.m
        return self.estado / self.m

    def uniforme(self, a, b):
        """Devuelve un flotante aleatorio entre a y b"""
        return a + (b - a) * self.aleatorio()

    def gauss(self, mu, sigma):
        """
        Aproximación de distribución Gaussiana usando el Teorema del Límite Central.
        Sumando 12 números aleatorios uniformes [0,1] da una distribución
        aproximando Normal(6, 1). Restando 6 da Normal(0, 1).
        """
        s = sum(self.aleatorio() for _ in range(12))
        return mu + sigma * (s - 6.0)

_rng = AleatorioSimple()

def exp(x):
    """
    Calcula e^x usando expansión de serie de Taylor:
    e^x = 1 + x + x^2/2! + x^3/3! + ...
    """
    # Manejar x negativo para mejor convergencia: e^-x = 1/e^x
    if x < 0:
        return 1.0 / exp(-x)
    
    # Serie de Taylor
    n = 20 # Número de términos
    resultado = 1.0
    termino = 1.0
    for i in range(1, n):
        termino *= x / i
        resultado += termino
    return resultado

def sin(x):
    """
    Calcula sin(x) usando serie de Taylor:
    sin(x) = x - x^3/3! + x^5/5! - ...
    """
    # Normalizar x a [-pi, pi] para mejor convergencia
    pi = 3.14159265358979323846
    x = x % (2 * pi)
    if x > pi:
        x -= 2 * pi
    
    n = 10 # Número de términos
    resultado = 0.0
    termino = x
    for i in range(1, n + 1):
        resultado += termino
        termino *= -1 * x * x / ((2 * i) * (2 * i + 1))
    return resultado

def cos(x):
    """
    Calcula cos(x) usando serie de Taylor:
    cos(x) = 1 - x^2/2! + x^4/4! - ...
    """
    # Normalizar x a [-pi, pi] para mejor convergencia
    pi = 3.14159265358979323846
    x = x % (2 * pi)
    if x > pi:
        x -= 2 * pi
    
    n = 10 # Número de términos
    resultado = 1.0
    termino = 1.0
    for i in range(1, n + 1):
        resultado += termino
        termino *= -1 * x * x / ((2 * i) * (2 * i + 1))
    return resultado

def tan(x):
    """
    Calcula tan(x) = sin(x) / cos(x)
    """
    return sin(x) / cos(x)

class Matriz:
    def __init__(self, datos):
        """
        Inicializa una Matriz.
        datos: Lista de listas de números.
        """
        if not isinstance(datos, list) or not all(isinstance(fila, list) for fila in datos):
            raise ValueError("Los datos deben ser una lista de listas")
        self.datos = datos
        self.filas = len(datos)
        self.columnas = len(datos[0]) if self.filas > 0 else 0

    def __repr__(self):
        return f"Matriz({self.filas}x{self.columnas})"

    def __str__(self):
        s = ""
        for fila in self.datos:
            s += "[" + ", ".join(f"{x:.4f}" for x in fila) + "]\n"
        return s

    def forma(self):
        return (self.filas, self.columnas)

    def __add__(self, otro):
        if isinstance(otro, Matriz):
            if self.forma() == otro.forma():
                nuevos_datos = [[self.datos[i][j] + otro.datos[i][j] for j in range(self.columnas)] for i in range(self.filas)]
                return Matriz(nuevos_datos)
            elif self.columnas == otro.columnas and otro.filas == 1:
                # Broadcast otro (1 fila) a self (N filas)
                nuevos_datos = [[self.datos[i][j] + otro.datos[0][j] for j in range(self.columnas)] for i in range(self.filas)]
                return Matriz(nuevos_datos)
            elif self.columnas == otro.columnas and self.filas == 1:
                # Broadcast self (1 fila) a otro (N filas)
                nuevos_datos = [[self.datos[0][j] + otro.datos[i][j] for j in range(self.columnas)] for i in range(otro.filas)]
                return Matriz(nuevos_datos)
            else:
                raise ValueError(f"Desajuste de forma para suma: {self.forma()} vs {otro.forma()}")
        elif isinstance(otro, (int, float)):
            nuevos_datos = [[self.datos[i][j] + otro for j in range(self.columnas)] for i in range(self.filas)]
            return Matriz(nuevos_datos)
        else:
            raise TypeError("Tipo de operando no soportado para +")

    def __sub__(self, otro):
        if isinstance(otro, Matriz):
            if self.forma() != otro.forma():
                raise ValueError(f"Desajuste de forma para resta: {self.forma()} vs {otro.forma()}")
            nuevos_datos = [[self.datos[i][j] - otro.datos[i][j] for j in range(self.columnas)] for i in range(self.filas)]
            return Matriz(nuevos_datos)
        elif isinstance(otro, (int, float)):
            nuevos_datos = [[self.datos[i][j] - otro for j in range(self.columnas)] for i in range(self.filas)]
            return Matriz(nuevos_datos)
        else:
            raise TypeError("Tipo de operando no soportado para -")

    def __mul__(self, otro):
        # Multiplicación elemento a elemento o escalar
        if isinstance(otro, Matriz):
            if self.forma() != otro.forma():
                raise ValueError(f"Desajuste de forma para mul elemento a elemento: {self.forma()} vs {otro.forma()}")
            nuevos_datos = [[self.datos[i][j] * otro.datos[i][j] for j in range(self.columnas)] for i in range(self.filas)]
            return Matriz(nuevos_datos)
        elif isinstance(otro, (int, float)):
            nuevos_datos = [[self.datos[i][j] * otro for j in range(self.columnas)] for i in range(self.filas)]
            return Matriz(nuevos_datos)
        else:
            raise TypeError("Tipo de operando no soportado para *")
    
    def __truediv__(self, otro):
        if isinstance(otro, (int, float)):
            nuevos_datos = [[self.datos[i][j] / otro for j in range(self.columnas)] for i in range(self.filas)]
            return Matriz(nuevos_datos)
        else:
            raise TypeError("Tipo de operando no soportado para /")

    def matmul(self, otro):
        if not isinstance(otro, Matriz):
            raise TypeError("Matmul requiere una Matriz")
        if self.columnas != otro.filas:
            raise ValueError(f"Desajuste de forma para matmul: {self.forma()} vs {otro.forma()}")
        
        # Multiplicación ingenua O(n^3)
        resultado = [[0 for _ in range(otro.columnas)] for _ in range(self.filas)]
        for i in range(self.filas):
            for j in range(otro.columnas):
                suma_val = 0
                for k in range(self.columnas):
                    suma_val += self.datos[i][k] * otro.datos[k][j]
                resultado[i][j] = suma_val
        return Matriz(resultado)

    def transpuesta(self):
        nuevos_datos = [[self.datos[j][i] for j in range(self.filas)] for i in range(self.columnas)]
        return Matriz(nuevos_datos)

    def aplicar(self, func):
        """Aplica una función elemento a elemento."""
        nuevos_datos = [[func(self.datos[i][j]) for j in range(self.columnas)] for i in range(self.filas)]
        return Matriz(nuevos_datos)

    def suma(self):
        """Suma de todos los elementos."""
        total = 0
        for fila in self.datos:
            total += sum(fila)
        return total

    def suma_eje_0(self):
        """Suma columnas (devuelve una Matriz 1xCols)."""
        resultado = [0] * self.columnas
        for fila in self.datos:
            for j in range(self.columnas):
                resultado[j] += fila[j]
        return Matriz([resultado])


    @staticmethod
    def ceros(filas, columnas):
        return Matriz([[0.0 for _ in range(columnas)] for _ in range(filas)])

    @staticmethod
    def normal_aleatoria(filas, columnas):
        """Distribución normal aleatoria."""
        return Matriz([[_rng.gauss(0, 1) for _ in range(columnas)] for _ in range(filas)])

    @staticmethod
    def uniforme(filas, columnas, a=0, b=1):
        return Matriz([[_rng.uniforme(a, b) for _ in range(columnas)] for _ in range(filas)])

def inversa(matriz):
    """Calcula la inversa usando eliminación de Gauss-Jordan."""
    if matriz.filas != matriz.columnas:
        raise ValueError("La matriz debe ser cuadrada para la inversa")
    
    n = matriz.filas
    # Aumentar con identidad
    aug = [fila[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, fila in enumerate(matriz.datos)]
    
    for i in range(n):
        # Encontrar pivote
        pivote = aug[i][i]
        if abs(pivote) < 1e-10:
            # Intercambiar con una fila inferior
            for k in range(i+1, n):
                if abs(aug[k][i]) > 1e-10:
                    aug[i], aug[k] = aug[k], aug[i]
                    pivote = aug[i][i]
                    break
            else:
                raise ValueError("La matriz es singular")
        
        # Normalizar fila pivote
        aug[i] = [x / pivote for x in aug[i]]
        
        # Eliminar otras filas
        for k in range(n):
            if k != i:
                factor = aug[k][i]
                aug[k] = [aug[k][j] - factor * aug[i][j] for j in range(2*n)]
    
    # Extraer inversa
    datos_inv = [fila[n:] for fila in aug]
    return Matriz(datos_inv)
