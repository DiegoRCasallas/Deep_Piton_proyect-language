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

// Python-like indentation handling is tricky in pure ANTLR without custom lexer logic.
// For simplicity in this DSL, we might rely on explicit tokens or a simplified structure first.
// However, the prompt asks for Python-like syntax.
// To handle indentation properly in ANTLR usually requires a custom TokenSource or pre-processing.
// Given the constraints and "simple syntax", I will use a simplified approach where blocks might use braces OR 
// I will assume the user provides code with some specific delimiters or I'll try to implement a basic indentation handler if possible.
// BUT, standard ANTLR grammars don't handle whitespace-sensitive indentation out of the box easily without target-language code.
// To stick to the "No external libraries" rule strictly for the *runtime* (math/dl), I can use ANTLR for parsing.
// I will use '{' and '}' for blocks in the underlying grammar to make it robust, 
// OR I will define INDENT/DEDENT tokens and assume a pre-processor or custom lexer emits them.
// Let's try to stick to a slightly more C-like structure for blocks if indentation is too complex, 
// OR use a pre-processing step in Python to convert indentation to INDENT/DEDENT tokens before feeding to ANTLR.
// Let's go with the Pre-processor approach for Indentation.
// So the grammar expects INDENT and DEDENT tokens.

INDENT: '<INDENT>';
DEDENT: '<DEDENT>';
