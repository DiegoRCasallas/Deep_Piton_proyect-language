# Generated from DeepPiton.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DeepPitonParser import DeepPitonParser
else:
    from DeepPitonParser import DeepPitonParser

# This class defines a complete listener for a parse tree produced by DeepPitonParser.
class DeepPitonListener(ParseTreeListener):

    # Enter a parse tree produced by DeepPitonParser#program.
    def enterProgram(self, ctx:DeepPitonParser.ProgramContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#program.
    def exitProgram(self, ctx:DeepPitonParser.ProgramContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#statement.
    def enterStatement(self, ctx:DeepPitonParser.StatementContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#statement.
    def exitStatement(self, ctx:DeepPitonParser.StatementContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#assignment.
    def enterAssignment(self, ctx:DeepPitonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#assignment.
    def exitAssignment(self, ctx:DeepPitonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#functionDef.
    def enterFunctionDef(self, ctx:DeepPitonParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#functionDef.
    def exitFunctionDef(self, ctx:DeepPitonParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#paramList.
    def enterParamList(self, ctx:DeepPitonParser.ParamListContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#paramList.
    def exitParamList(self, ctx:DeepPitonParser.ParamListContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#block.
    def enterBlock(self, ctx:DeepPitonParser.BlockContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#block.
    def exitBlock(self, ctx:DeepPitonParser.BlockContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#ifStmt.
    def enterIfStmt(self, ctx:DeepPitonParser.IfStmtContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#ifStmt.
    def exitIfStmt(self, ctx:DeepPitonParser.IfStmtContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#whileStmt.
    def enterWhileStmt(self, ctx:DeepPitonParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#whileStmt.
    def exitWhileStmt(self, ctx:DeepPitonParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#forStmt.
    def enterForStmt(self, ctx:DeepPitonParser.ForStmtContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#forStmt.
    def exitForStmt(self, ctx:DeepPitonParser.ForStmtContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#returnStmt.
    def enterReturnStmt(self, ctx:DeepPitonParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#returnStmt.
    def exitReturnStmt(self, ctx:DeepPitonParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#expressionStmt.
    def enterExpressionStmt(self, ctx:DeepPitonParser.ExpressionStmtContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#expressionStmt.
    def exitExpressionStmt(self, ctx:DeepPitonParser.ExpressionStmtContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#PowerExpr.
    def enterPowerExpr(self, ctx:DeepPitonParser.PowerExprContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#PowerExpr.
    def exitPowerExpr(self, ctx:DeepPitonParser.PowerExprContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#FunctionCallExpr.
    def enterFunctionCallExpr(self, ctx:DeepPitonParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#FunctionCallExpr.
    def exitFunctionCallExpr(self, ctx:DeepPitonParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:DeepPitonParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:DeepPitonParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#ComparisonExpr.
    def enterComparisonExpr(self, ctx:DeepPitonParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#ComparisonExpr.
    def exitComparisonExpr(self, ctx:DeepPitonParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#AtomExpr.
    def enterAtomExpr(self, ctx:DeepPitonParser.AtomExprContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#AtomExpr.
    def exitAtomExpr(self, ctx:DeepPitonParser.AtomExprContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#TransposeExpr.
    def enterTransposeExpr(self, ctx:DeepPitonParser.TransposeExprContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#TransposeExpr.
    def exitTransposeExpr(self, ctx:DeepPitonParser.TransposeExprContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:DeepPitonParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:DeepPitonParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#InverseExpr.
    def enterInverseExpr(self, ctx:DeepPitonParser.InverseExprContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#InverseExpr.
    def exitInverseExpr(self, ctx:DeepPitonParser.InverseExprContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#MatrixMulExpr.
    def enterMatrixMulExpr(self, ctx:DeepPitonParser.MatrixMulExprContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#MatrixMulExpr.
    def exitMatrixMulExpr(self, ctx:DeepPitonParser.MatrixMulExprContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#UnaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:DeepPitonParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#UnaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:DeepPitonParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#MethodCallExpr.
    def enterMethodCallExpr(self, ctx:DeepPitonParser.MethodCallExprContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#MethodCallExpr.
    def exitMethodCallExpr(self, ctx:DeepPitonParser.MethodCallExprContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#argList.
    def enterArgList(self, ctx:DeepPitonParser.ArgListContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#argList.
    def exitArgList(self, ctx:DeepPitonParser.ArgListContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#IdAtom.
    def enterIdAtom(self, ctx:DeepPitonParser.IdAtomContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#IdAtom.
    def exitIdAtom(self, ctx:DeepPitonParser.IdAtomContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#NumberAtom.
    def enterNumberAtom(self, ctx:DeepPitonParser.NumberAtomContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#NumberAtom.
    def exitNumberAtom(self, ctx:DeepPitonParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#StringAtom.
    def enterStringAtom(self, ctx:DeepPitonParser.StringAtomContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#StringAtom.
    def exitStringAtom(self, ctx:DeepPitonParser.StringAtomContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#ParenAtom.
    def enterParenAtom(self, ctx:DeepPitonParser.ParenAtomContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#ParenAtom.
    def exitParenAtom(self, ctx:DeepPitonParser.ParenAtomContext):
        pass


    # Enter a parse tree produced by DeepPitonParser#ListLiteral.
    def enterListLiteral(self, ctx:DeepPitonParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by DeepPitonParser#ListLiteral.
    def exitListLiteral(self, ctx:DeepPitonParser.ListLiteralContext):
        pass



del DeepPitonParser