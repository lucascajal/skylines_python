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
        #result.printSkyline()
        result.saveImage()
        return result.getMeasures()

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
        
        # City
        if len(l) == 7:
            sk = Skyline()
            sk.addBuilding((int(l[1].getText()), int(l[3].getText()), int(l[5].getText())))
            return sk

        # Random cities
        elif len(l) == 11:
            sk = Skyline()
            sk.addRandom(int(l[1].getText()), int(l[3].getText()), int(l[5].getText()), int(l[7].getText()), int(l[9].getText()))
            return sk
        
        # Other operators
        elif len(l) == 3:
            # Assignation
            if l[1].getText() == ':=':
                res = self.visit(l[2])
                self.dictionary[l[0].getText()] = res
                return res

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

'''
    def visitSkyline(self, ctx:SkylineParser.SkylineContext):
        l = [n for n in ctx.getChildren()]
        # City
        if len(l) == 7:
            sk = Skyline()
            sk.addBuilding((self.visit(l[1]), self.visit(l[3]), self.visit(l[5])))
            return sk

        # Random cities
        elif len(l) == 11:
            sk = Skyline()
            sk.addRandom(self.visit(l[1]), self.visit(l[3]), self.visit(l[5]), self.visit(l[7]), self.visit(l[9]))
            return sk
'''