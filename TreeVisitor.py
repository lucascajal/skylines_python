if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor
class TreeVisitor(SkylineVisitor):
    def __init__(self):
        self.nivell = 0
    def visitExpr(self, ctx:SkylineParser.ExprContext):
        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            print("  " * self.nivell +
                  SkylineParser.symbolicNames[n.getSymbol().type] +
                  '(' +n.getText() + ')')
            self.nivell -= 1
        elif ctx.getChildCount() == 3:
            l = [n for n in ctx.getChildren()]
            print('  ' *  self.nivell + 'MES(+)')
            print('-TEST: ' + ctx.expr(0))
            self.nivell += 1
            self.visit(ctx.expr(0))
            self.nivell += 1
            self.visit(ctx.expr(1))
            self.nivell -= 1