grammar DeepPiton;

// Parser Rules

program: statement* EOF;

statement
    : assignment
    | functionDef
    | ifStmt
    | whileStmt
    | forStmt
    | expressionStmt
    | returnStmt
    ;

assignment: ID '=' expression;

functionDef: 'def' ID '(' (paramList)? ')' ':' block;

paramList: ID (',' ID)*;

block: INDENT statement+ DEDENT;

ifStmt: 'if' expression ':' block ('elif' expression ':' block)* ('else' ':' block)?;

whileStmt: 'while' expression ':' block;

forStmt: 'for' ID 'in' expression ':' block;

returnStmt: 'return' expression?;

expressionStmt: expression;

expression
    : expression '**' expression              # PowerExpr
    | '-' expression                          # UnaryMinusExpr
    | expression ('*' | '/' | '%') expression # MulDivExpr
    | expression ('+' | '-') expression       # AddSubExpr
    | expression ('@') expression             # MatrixMulExpr
    | expression COMPARISON_OP expression     # ComparisonExpr
    | 'TRP' '(' expression ')'                # TransposeExpr
    | 'INV' '(' expression ')'                # InverseExpr
    | expression '.' ID '(' (argList)? ')'    # MethodCallExpr
    | ID '(' (argList)? ')'                   # FunctionCallExpr
    | atom                                    # AtomExpr
    ;

argList: expression (',' expression)*;

atom
    : ID                                       # IdAtom
    | NUMBER                                   # NumberAtom
    | STRING                                   # StringAtom
    | '(' expression ')'                       # ParenAtom
    | '[' (expression (',' expression)*)? ']'  # ListLiteral
    ;

// Lexer Rules

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' .*? '"';

COMPARISON_OP: '==' | '!=' | '<' | '>' | '<=' | '>=';

NEWLINE: [\r\n]+ -> skip;
WS: [ \t]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;

//El manejo de la sangría similar al de Python es complicado en ANTLR puro sin lógica de análisis léxico personalizada.
// Para simplificar este DSL, podríamos usar primero tokens explícitos o una estructura simplificada.
// Para manejar la sangría correctamente en ANTLR, generalmente se requiere un TokenSource personalizado o preprocesamiento.
// Entonces, la gramática espera tokens INDENT y DEDENT.


INDENT: '<INDENT>';
DEDENT: '<DEDENT>';
