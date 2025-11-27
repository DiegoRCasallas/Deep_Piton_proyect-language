import sys
from src.parser.DeepPitonVisitor import DeepPitonVisitor
from src.parser.DeepPitonParser import DeepPitonParser
from src.math_core import Matriz, inversa
from src.dl_core import Densa, Modelo
from src.utils import cargar_csv, guardar_texto, graficar_dispersion_ascii

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class DeepPitonVisitorImpl(DeepPitonVisitor):
    def __init__(self):
        self.globals = {}
        self.scopes = [self.globals]
        self.functions = {}
        self._setup_builtins()

    def _setup_builtins(self):
        self.builtins = {
            'print': print,
            'CARGAR_CSV': cargar_csv,
            'GUARDAR_TEXTO': guardar_texto,
            'GRAFICAR_DISPERSION': lambda x, y, pred=None: graficar_dispersion_ascii(self._to_matrix(x), self._to_matrix(y), self._to_matrix(pred) if pred else None),
            'CAPA_DENSA': Densa,
            'MODELO': Modelo, # Constructor para Modelo
            'REGRESION_LINEAL': self._regresion_lineal_wrapper, # Constructor para RegresionLineal
            'ENTRENAR': self._train_wrapper,
            'AJUSTAR': self._fit_wrapper,
            'MM': lambda a, b: self._to_matrix(a).matmul(self._to_matrix(b)),
            'TRP': lambda a: self._to_matrix(a).transpuesta(),
            'INV': lambda a: inversa(self._to_matrix(a)),
            'len': len,
            'range': range,
            'int': int,
            'float': float,
            'str': str,
            'MATRIZ': Matriz
        }

    def _regresion_lineal_wrapper(self):
        from src.dl_core import RegresionLineal
        return RegresionLineal()

    def _fit_wrapper(self, modelo, X, Y):
        from src.dl_core import RegresionLineal
        if isinstance(modelo, RegresionLineal):
            modelo.ajustar(self._to_matrix(X), self._to_matrix(Y))
        else:
             raise TypeError("El primer argumento para AJUSTAR debe ser un modelo de Regresión Lineal")

    def _train_wrapper(self, modelo, X, Y, epocas, lr):
        if not isinstance(modelo, Modelo):
            raise TypeError("El primer argumento para ENTRENAR debe ser un Modelo")
        modelo.entrenar(self._to_matrix(X), self._to_matrix(Y), int(epocas), float(lr))

    def current_scope(self):
        return self.scopes[-1]

    def visitProgram(self, ctx: DeepPitonParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitAssignment(self, ctx: DeepPitonParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.current_scope()[var_name] = value
        return value

    def visitIdAtom(self, ctx: DeepPitonParser.IdAtomContext):
        var_name = ctx.ID().getText()
        if var_name in self.current_scope():
            return self.current_scope()[var_name]
        elif var_name in self.globals:
            return self.globals[var_name]
        elif var_name in self.builtins:
            return self.builtins[var_name]
        elif var_name in self.functions:
            return self.functions[var_name]
        else:
            raise NameError(f"Nombre '{var_name}' no está definido")

    def visitNumberAtom(self, ctx: DeepPitonParser.NumberAtomContext):
        text = ctx.getText()
        if '.' in text:
            return float(text)
        return int(text)

    def visitStringAtom(self, ctx: DeepPitonParser.StringAtomContext):
        return ctx.getText().strip('"')

    def visitListLiteral(self, ctx: DeepPitonParser.ListLiteralContext):
        elements = []
        if ctx.expression():
            for expr in ctx.expression():
                elements.append(self.visit(expr))
        return elements

    def visitAddSubExpr(self, ctx: DeepPitonParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '+':
            return left + right
        else:
            return left - right

    def visitMulDivExpr(self, ctx: DeepPitonParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        if op == '*':
            return left * right
        elif op == '/':
            return left / right
        elif op == '%':
            return left % right

    def visitPowerExpr(self, ctx: DeepPitonParser.PowerExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left ** right

    def _to_matrix(self, val):
        if isinstance(val, Matriz):
            return val
        if isinstance(val, list):
            # Check if it's a list of lists (2D) or list of numbers (1D -> Row vector)
            if not val:
                return Matriz([])
            if isinstance(val[0], list):
                return Matriz(val)
            else:
                return Matriz([val]) # Treat 1D list as 1xN matrix
        raise TypeError(f"No se puede convertir {type(val)} a Matriz")

    def visitMatrixMulExpr(self, ctx: DeepPitonParser.MatrixMulExprContext):
        left = self._to_matrix(self.visit(ctx.expression(0)))
        right = self._to_matrix(self.visit(ctx.expression(1)))
        return left.matmul(right)

    def visitTransposeExpr(self, ctx: DeepPitonParser.TransposeExprContext):
        arg = self._to_matrix(self.visit(ctx.expression()))
        return arg.transpuesta()

    def visitInverseExpr(self, ctx: DeepPitonParser.InverseExprContext):
        arg = self._to_matrix(self.visit(ctx.expression()))
        return inversa(arg)

    def visitComparisonExpr(self, ctx: DeepPitonParser.ComparisonExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.COMPARISON_OP().getText()
        if op == '==': return left == right
        if op == '!=': return left != right
        if op == '<': return left < right
        if op == '>': return left > right
        if op == '<=': return left <= right
        if op == '>=': return left >= right

    def visitIfStmt(self, ctx: DeepPitonParser.IfStmtContext):
        # Check if condition
        conditions = ctx.expression()
        blocks = ctx.block()
        
        for i, cond in enumerate(conditions):
            if self.visit(cond):
                self.visit(blocks[i])
                return
        
        # Else block (last block if mismatch count)
        if len(blocks) > len(conditions):
            self.visit(blocks[-1])

    def visitWhileStmt(self, ctx: DeepPitonParser.WhileStmtContext):
        while self.visit(ctx.expression()):
            self.visit(ctx.block())

    def visitForStmt(self, ctx: DeepPitonParser.ForStmtContext):
        var_name = ctx.ID().getText()
        iterable = self.visit(ctx.expression())
        
        # If iterable is a Matrix, iterate over rows? Or elements?
        # Standard python iterates over list.
        # If it's a Matrix, let's iterate over rows (as lists or sub-matrices).
        # For simplicity, assume iterable is list or range.
        
        if isinstance(iterable, Matriz):
            # Iterate rows
            iterator = iterable.datos
        else:
            iterator = iterable

        for item in iterator:
            self.current_scope()[var_name] = item
            self.visit(ctx.block())

    def visitFunctionDef(self, ctx: DeepPitonParser.FunctionDefContext):
        func_name = ctx.ID().getText()
        params = []
        if ctx.paramList():
            params = [node.getText() for node in ctx.paramList().ID()]
        
        self.functions[func_name] = {'params': params, 'block': ctx.block()}
        return None

    def visitFunctionCallExpr(self, ctx: DeepPitonParser.FunctionCallExprContext):
        func_name = ctx.ID().getText()
        args = []
        if ctx.argList():
            for expr in ctx.argList().expression():
                args.append(self.visit(expr))
        
        # Check builtins
        if func_name in self.builtins:
            return self.builtins[func_name](*args)
        
        # Check user functions
        if func_name in self.functions:
            func_def = self.functions[func_name]
            params = func_def['params']
            block = func_def['block']
            
            if len(args) != len(params):
                raise TypeError(f"La función {func_name} espera {len(params)} argumentos, obtuvo {len(args)}")
            
            # Create new scope
            new_scope = {k: v for k, v in zip(params, args)}
            self.scopes.append(new_scope)
            
            ret_val = None
            try:
                self.visit(block)
            except ReturnException as e:
                ret_val = e.value
            finally:
                self.scopes.pop()
            
            return ret_val
            
        raise NameError(f"La función '{func_name}' no está definida")

    def visitMethodCallExpr(self, ctx: DeepPitonParser.MethodCallExprContext):
        obj = self.visit(ctx.expression())
        method_name = ctx.ID().getText()
        args = []
        if ctx.argList():
            for expr in ctx.argList().expression():
                args.append(self.visit(expr))
        
        # Traducir nombres de métodos de DeepPiton a métodos internos en español si es necesario
        # Por ahora, asumimos que el usuario usa los nombres en español definidos en las clases
        
        if hasattr(obj, method_name):
            method = getattr(obj, method_name)
            if callable(method):
                # Si el método es 'predecir', necesitamos convertir el argumento a Matriz
                if method_name == 'predecir' and len(args) == 1:
                     args[0] = self._to_matrix(args[0])
                return method(*args)
            else:
                raise TypeError(f"La propiedad '{method_name}' no es invocable")
        else:
            # Intento de mapeo si el usuario usa nombres en inglés por error (opcional, pero buena práctica)
            # map_methods = {'forward': 'adelante', 'train': 'entrenar', 'add': 'agregar'}
            # if method_name in map_methods and hasattr(obj, map_methods[method_name]):
            #     return getattr(obj, map_methods[method_name])(*args)
            
            raise AttributeError(f"El objeto {obj} no tiene el método '{method_name}'")

    def visitReturnStmt(self, ctx: DeepPitonParser.ReturnStmtContext):
        value = None
        if ctx.expression():
            value = self.visit(ctx.expression())
        raise ReturnException(value)

    def visitBlock(self, ctx: DeepPitonParser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)
