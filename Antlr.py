import sys, traceback
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from TreeVisitor import TreeVisitor
from EvalVisitor import EvalVisitor

class SkyilineNotAssigned(Exception):
   """Raised when trying to access a non existing skyline"""
   pass

class WrongDimensions(Exception):
   """Raised when trying to create a building with wrong parameters"""
   pass

class Antlr():
   def __init__(self, initialBuildings={}):
      self.visitor = EvalVisitor()

   def send(self, text):
      try:
         input_stream = InputStream(text)
         lexer = SkylineLexer(input_stream)
         token_stream = CommonTokenStream(lexer)
         parser = SkylineParser(token_stream)
         tree = parser.root()
         self.visitor.visit(tree)
         return True
      except Exception as e:
         print('error')
         traceback.print_exc()
         return False
      '''
      except SkyilineNotAssigned:
         print("SkyilineNotAssigned")
         return False
      except WrongDimensions:
         print("WrongDimensions")
         return False
      except Exception as e:
         print(e)
         return False
      '''
      

def main():
   visitor = EvalVisitor()

   while True:
      input_stream = InputStream(input('? '))
      lexer = SkylineLexer(input_stream)
      token_stream = CommonTokenStream(lexer)
      parser = SkylineParser(token_stream)
      tree = parser.root()
      visitor.visit(tree)
   
if __name__ == '__main__':
    main()