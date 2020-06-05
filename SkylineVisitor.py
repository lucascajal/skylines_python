# Generated from Skyline.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#expr.
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#building.
    def visitBuilding(self, ctx:SkylineParser.BuildingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#buildings.
    def visitBuildings(self, ctx:SkylineParser.BuildingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#var.
    def visitVar(self, ctx:SkylineParser.VarContext):
        return self.visitChildren(ctx)



del SkylineParser