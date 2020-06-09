#!/usr/bin/env python3

from Skyline import Skyline
from Skyline import WrongDimensions
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor


class SkyilineNotAssigned(Exception):
    """Implements the SkyilineNotAssigned exception, raised when
    the user makes a reference to a not instantiated skyline.
    """
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'SkyilineNotAssigned, {0}'.format(self.message)
        else:
            return 'SkyilineNotAssigned has been raised'


class EvalVisitor(SkylineVisitor):
    def __init__(self):
        """Class constructor, declares an empty symbol table"""
        self.dictionary = {}

    def listKeys(self):
        """Returns all the instantiated skylines name's"""
        return self.dictionary.keys()

    def getDictionary(self):
        """Returns the symbol table"""
        return self.dictionary

    def addToDictionary(self, name, skyline):
        """Adds a new instantiated skyline to the symbol table"""
        self.dictionary[name] = skyline

    def getArea(self, id):
        """Returns the area for skyline 'id'"""
        area, height = self.dictionary[id].getMeasures()
        return area

    def visitRoot(self, ctx: SkylineParser.RootContext):
        """Visitor for root rule in grammar, returns a skyline"""
        n = next(ctx.getChildren())
        result = self.visit(n)
        return result

    def visitBuilding(self, ctx: SkylineParser.BuildingContext):
        """Visitor for building rule in grammar, returns a new skyline"""
        l = [n for n in ctx.getChildren()]
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

    def visitBuildings(self, ctx: SkylineParser.BuildingsContext):
        """Visitor for buildings rule in grammar, returns a new skyline"""
        l = [n for n in ctx.getChildren()]
        # City
        sk = Skyline()
        for i in range(1, len(l), 2):
            sk = sk + self.visit(l[i])
        return sk

    def visitVar(self, ctx: SkylineParser.VarContext):
        """Visitor for var rule in grammar, returns an instantiated skyline.
        If the referenced skyline is not instantiated, raises 'SkyilineNotAssigned'.
        """
        n = next(ctx.getChildren())
        text = n.getText()
        if text in self.dictionary:
            return self.dictionary[text]
        else:
            raise SkyilineNotAssigned

    def visitNumber(self, ctx: SkylineParser.NumberContext):
        """Visitor for number rule in grammar, returns an integer"""
        n = next(ctx.getChildren())
        text = n.getText()
        return int(text)

    def visitExpr(self, ctx: SkylineParser.ExprContext):
        """Visitor for expr rule in grammar, returns a skyline"""
        l = [n for n in ctx.getChildren()]
        # Building, buildings, num or word
        if len(l) == 1:
            return self.visit(l[0])

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
