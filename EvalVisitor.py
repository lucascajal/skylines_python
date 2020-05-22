from Skyline import Skyline
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor

class SkyilineNotAssigned(Exception):
   """Raised when trying to access a non existing skyline"""
   pass

class EvalVisitor(SkylineVisitor):
    def __init__(self):
        self.dictionary = {}

    def visitRoot(self, ctx:SkylineParser.RootContext):
        n = next(ctx.getChildren())
        result = self.visit(n)
        if result != None:
            print(result)

    def visitExpr(self, ctx:SkylineParser.ExprContext):
        l = [n for n in ctx.getChildren()]
        # Num or word
        if len(l) == 1:
            text = l[0].getText()
            try:
                return int(text) # the value is a number
            except ValueError:
                if text in self.dictionary:
                    return self.dictionary[text]
                else:
                    raise SkyilineNotAssigned
            
        
        # Mirror
        elif len(l) == 2:
            return - self.visit(l[1])

        # Other operators
        elif len(l) == 3:
            # Assignation
            if l[1].getText() == ':=':
                self.dictionary[l[0].getText()] = self.visit(l[2])

            # Parenthesis
            if l[0].getText() == '(':
                return self.visit(l[1])

            # Sum
            elif l[1].getText() == '+':
                return self.visit(l[0]) + self.visit(l[2])
            
            # Subtraction
            elif l[1].getText() == '-':
                return self.visit(l[0]) - self.visit(l[2])

            # Multiplication
            elif l[1].getText() == '*':
                return self.visit(l[0]) * self.visit(l[2])