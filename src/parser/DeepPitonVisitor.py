# Generated from DeepPiton.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DeepPitonParser import DeepPitonParser
else:
    from DeepPitonParser import DeepPitonParser

# This class defines a complete generic visitor for a parse tree produced by DeepPitonParser.

class DeepPitonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DeepPitonParser#program.
    def visitProgram(self, ctx:DeepPitonParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#statement.
    def visitStatement(self, ctx:DeepPitonParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#assignment.
    def visitAssignment(self, ctx:DeepPitonParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#functionDef.
    def visitFunctionDef(self, ctx:DeepPitonParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#paramList.
    def visitParamList(self, ctx:DeepPitonParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#block.
    def visitBlock(self, ctx:DeepPitonParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#ifStmt.
    def visitIfStmt(self, ctx:DeepPitonParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#whileStmt.
    def visitWhileStmt(self, ctx:DeepPitonParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#forStmt.
    def visitForStmt(self, ctx:DeepPitonParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#returnStmt.
    def visitReturnStmt(self, ctx:DeepPitonParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#expressionStmt.
    def visitExpressionStmt(self, ctx:DeepPitonParser.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#PowerExpr.
    def visitPowerExpr(self, ctx:DeepPitonParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:DeepPitonParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:DeepPitonParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#ComparisonExpr.
    def visitComparisonExpr(self, ctx:DeepPitonParser.ComparisonExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#AtomExpr.
    def visitAtomExpr(self, ctx:DeepPitonParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#TransposeExpr.
    def visitTransposeExpr(self, ctx:DeepPitonParser.TransposeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:DeepPitonParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#InverseExpr.
    def visitInverseExpr(self, ctx:DeepPitonParser.InverseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#MatrixMulExpr.
    def visitMatrixMulExpr(self, ctx:DeepPitonParser.MatrixMulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:DeepPitonParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#MethodCallExpr.
    def visitMethodCallExpr(self, ctx:DeepPitonParser.MethodCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#argList.
    def visitArgList(self, ctx:DeepPitonParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#IdAtom.
    def visitIdAtom(self, ctx:DeepPitonParser.IdAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#NumberAtom.
    def visitNumberAtom(self, ctx:DeepPitonParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#StringAtom.
    def visitStringAtom(self, ctx:DeepPitonParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#ParenAtom.
    def visitParenAtom(self, ctx:DeepPitonParser.ParenAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DeepPitonParser#ListLiteral.
    def visitListLiteral(self, ctx:DeepPitonParser.ListLiteralContext):
        return self.visitChildren(ctx)



del DeepPitonParser