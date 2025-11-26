# import math
from src.math_core import Matriz, exp, inversa

class Activacion:
    def adelante(self, x):
        raise NotImplementedError
    def derivada(self, x):
        raise NotImplementedError

class Sigmoide(Activacion):
    def adelante(self, x):
        return x.aplicar(lambda v: 1 / (1 + exp(-v)))
    
    def derivada(self, x):
        # s * (1 - s)
        s = self.adelante(x)
        return s.aplicar(lambda v: v * (1 - v)) # Esto está mal si x ya está activado.
        # Usualmente la derivada toma la entrada o la salida.
        # Asumamos que la derivada toma la salida de la capa (valor activado) para sigmoide?
        # O lo calculamos desde la entrada.
        # Calculémoslo desde la entrada x para estar seguros.
        # s(x) * (1 - s(x))

class ReLU(Activacion):
    def adelante(self, x):
        return x.aplicar(lambda v: max(0, v))
    
    def derivada(self, x):
        return x.aplicar(lambda v: 1.0 if v > 0 else 0.0)

class Capa:
    def adelante(self, datos_entrada):
        raise NotImplementedError
    def atras(self, grad_salida, tasa_aprendizaje):
        raise NotImplementedError

class Densa(Capa):
    def __init__(self, tamano_entrada, tamano_salida, activacion='relu'):
        self.pesos = Matriz.normal_aleatoria(tamano_entrada, tamano_salida)
        self.sesgo = Matriz.ceros(1, tamano_salida)
        self.nombre_activacion = activacion
        if activacion == 'sigmoid':
            self.activacion = Sigmoide()
        elif activacion == 'relu':
            self.activacion = ReLU()
        else:
            self.activacion = None # Lineal
        
        self.cache_entrada = None
        self.salida_pre_activacion = None

    def adelante(self, datos_entrada):
        self.cache_entrada = datos_entrada
        self.salida_pre_activacion = datos_entrada.matmul(self.pesos) + self.sesgo
        
        if self.activacion:
            return self.activacion.adelante(self.salida_pre_activacion)
        return self.salida_pre_activacion

    def atras(self, grad_salida, tasa_aprendizaje):
        # grad_salida es dL/dY
        
        # Si hay activación, aplicar regla de la cadena: dL/dZ = dL/dY * dY/dZ
        if self.activacion:
            d_activacion = self.activacion.derivada(self.salida_pre_activacion)
            grad_pre = grad_salida * d_activacion # Elemento a elemento
        else:
            grad_pre = grad_salida
            
        # dL/dW = X.T @ dL/dZ
        grad_pesos = self.cache_entrada.transpuesta().matmul(grad_pre)
        
        # dL/db = sum(dL/dZ, axis=0)
        grad_sesgo = grad_pre.suma_eje_0()
        
        # dL/dX = dL/dZ @ W.T
        grad_entrada = grad_pre.matmul(self.pesos.transpuesta())
        
        # Actualizar pesos y sesgos
        # W = W - lr * grad_pesos
        self.pesos = self.pesos - (grad_pesos * tasa_aprendizaje)
        self.sesgo = self.sesgo - (grad_sesgo * tasa_aprendizaje)
        
        return grad_entrada

class ECM:
    def perdida(self, y_verdadero, y_predicho):
        # Error Cuadrático Medio: 1/N * sum((y_verdadero - y_predicho)^2)
        diferencia = y_verdadero - y_predicho
        cuad_diferencia = diferencia.aplicar(lambda v: v**2)
        return cuad_diferencia.suma() / y_verdadero.filas

    def derivada(self, y_verdadero, y_predicho):
        # Derivada de ECM respecto a y_predicho: -2/N * (y_verdadero - y_predicho)
        # O simplemente (y_predicho - y_verdadero) * 2/N
        n = y_verdadero.filas
        diferencia = y_predicho - y_verdadero
        return diferencia * (2.0 / n)

class Modelo:
    def __init__(self):
        self.capas = []

    def agregar(self, capa):
        self.capas.append(capa)

    def adelante(self, x):
        if isinstance(x, list):
            # Importar Matriz aquí para evitar importación circular si la hay, o asumir que está disponible
            from src.math_core import Matriz
            if not x:
                x = Matriz([])
            elif isinstance(x[0], list):
                x = Matriz(x)
            else:
                x = Matriz([x])
        
        salida = x
        for capa in self.capas:
            salida = capa.adelante(salida)
        return salida

    def entrenar(self, x_entrenamiento, y_entrenamiento, epocas, lr):
        fn_perdida = ECM()
        for epoca in range(epocas):
            # Adelante
            y_predicho = self.adelante(x_entrenamiento)
            
            # Perdida
            perdida = fn_perdida.perdida(y_entrenamiento, y_predicho)
            
            # Atras
            grad = fn_perdida.derivada(y_entrenamiento, y_predicho)
            for capa in reversed(self.capas):
                grad = capa.atras(grad, lr)
            
            if epoca % 100 == 0:
                print(f"Epoca {epoca}, Perdida: {perdida:.6f}")

class RegresionLineal:
    def __init__(self):
        self.pesos = None

    def ajustar(self, X, Y):
        # Ecuación Normal: theta = (X^T * X)^-1 * X^T * y
        # Asumimos que X ya tiene el término de sesgo (columna de 1s) si es necesario,
        # o el usuario debe agregarlo. Para simplificar, agregaremos sesgo aquí.
        
        # Agregar columna de 1s a X para el sesgo
        filas = X.filas
        unos = [[1.0] for _ in range(filas)]
        matriz_unos = Matriz(unos)
        
        # Concatenar 1s a X (esto requiere implementar concatenación en Matriz, 
        # pero como no tenemos, hagámoslo manualmente manipulando los datos)
        datos_aumentados = [fila_x + [1.0] for fila_x in X.datos]
        X_b = Matriz(datos_aumentados)
        
        # Calcular theta
        # (X_b^T * X_b)
        Xt = X_b.transpuesta()
        XtX = Xt.matmul(X_b)
        
        # Inversa
        try:
            XtX_inv = inversa(XtX)
        except ValueError:
            print("Error: La matriz es singular, no se puede invertir.")
            return

        # XtX_inv * Xt * Y
        self.pesos = XtX_inv.matmul(Xt).matmul(Y)

    def predecir(self, X):
        if self.pesos is None:
            raise Exception("El modelo no ha sido ajustado")
            
        # Agregar columna de 1s a X
        datos_aumentados = [fila_x + [1.0] for fila_x in X.datos]
        X_b = Matriz(datos_aumentados)
        
        return X_b.matmul(self.pesos)

