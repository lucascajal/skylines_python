import sys
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from TreeVisitor import TreeVisitor
from EvalVisitor import EvalVisitor

class SkyilineNotAssigned(Exception):
   """Raised when trying to access a non existing skyline"""
   pass

visitor = EvalVisitor()

while True:
    input_stream = InputStream(input('? '))
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()
    visitor.visit(tree)