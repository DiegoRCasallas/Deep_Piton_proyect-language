import sys
from antlr4 import *
from src.parser.DeepPitonLexer import DeepPitonLexer
from src.parser.DeepPitonParser import DeepPitonParser
from src.visitor import DeepPitonVisitorImpl

def preprocesar_indentacion(codigo_fuente):
    lineas = codigo_fuente.split('\n')
    lineas_procesadas = []
    pila_indentacion = [0]
    
    for linea in lineas:
        despojada = linea.strip()
        if not despojada:
            continue # Saltar lineas vacias
            
        # Calcular indentación (asumiendo espacios)
        indentacion = len(linea) - len(linea.lstrip())
        
        if indentacion > pila_indentacion[-1]:
            pila_indentacion.append(indentacion)
            lineas_procesadas.append('<INDENT>')
            lineas_procesadas.append(despojada)
        elif indentacion < pila_indentacion[-1]:
            while indentacion < pila_indentacion[-1]:
                pila_indentacion.pop()
                lineas_procesadas.append('<DEDENT>')
            if indentacion != pila_indentacion[-1]:
                raise IndentationError("La desindentación no coincide con ningún nivel de indentación externo")
            lineas_procesadas.append(despojada)
        else:
            lineas_procesadas.append(despojada)
            
    # Cerrar indentaciones restantes
    while len(pila_indentacion) > 1:
        pila_indentacion.pop()
        lineas_procesadas.append('<DEDENT>')
        
    return '\n'.join(lineas_procesadas)

def principal(argv):
    if len(argv) < 2:
        print("Uso: python deep_piton.py <archivo.dp>")
        return

    archivo_entrada = argv[1]
    with open(archivo_entrada, 'r') as f:
        codigo_fuente = f.read()

    # Preprocesar indentación
    try:
        # Nota: Mi gramática espera tokens NEWLINE. 
        # El preprocesador une con \n, así que los NEWLINE están ahí.
        # Pero la regla de gramática `block: NEWLINE INDENT statement+ DEDENT;`
        # espera un NEWLINE antes de INDENT.
        # Mi preprocesador pone INDENT en una nueva línea.
        # Ajustemos el preprocesador para ser compatible con la gramática.
        # En realidad, alimentemos el código preprocesado.
        # El Lexer define NEWLINE: [\r\n]+ -> skip;
        # Espera, si NEWLINE se salta, entonces `block: NEWLINE ...` fallará porque el parser no verá NEWLINE.
        # Necesito eliminar `NEWLINE` de la regla `block` en la gramática o hacer que NEWLINE no se salte.
        # En la gramática: `NEWLINE: [\r\n]+ -> skip;`
        # Así que la regla `block` NO debería tener `NEWLINE`.
        # Arreglaré la gramática primero.
        pass
    except Exception as e:
        print(f"Error de Preprocesador: {e}")
        return

    # Arreglaré la gramática en un paso separado, pero por ahora asumamos que la arreglaré.
    # Continuemos con la función principal.
    
    codigo_procesado = preprocesar_indentacion(codigo_fuente)
    # print("DEBUG: Código Procesado:\n", codigo_procesado)

    flujo_entrada = InputStream(codigo_procesado)
    lexer = DeepPitonLexer(flujo_entrada)
    stream = CommonTokenStream(lexer)
    parser = DeepPitonParser(stream)
    arbol = parser.program()

    visitante = DeepPitonVisitorImpl()
    try:
        visitante.visit(arbol)
    except Exception as e:
        print(f"Error en Tiempo de Ejecución: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    principal(sys.argv)
