import sys, traceback, pickle
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
         return self.visitor.visit(tree)
      except Exception as e:
         print('error')
         return False, False
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
   
   def lst(self):
      return self.visitor.listKeys()

   def getArea(self, id):
      return self.visitor.getArea(id)
   
   def clean(self):
      self.visitor = EvalVisitor()
   
   def save(self, name):
      data = self.visitor.getDictionary()
      pickle_file = open('/home/lucas/upc/LP/Python/bot/'+ name +'.sky', 'wb')
      pickle.dump(data, pickle_file)
      pickle_file.close()
   
   def load(self, name):
      pickle_file = open('/home/lucas/upc/LP/Python/bot/'+ name +'.sky', 'rb')
      data = pickle.load(pickle_file)
      pickle_file.close()
      self.visitor = EvalVisitor(data)

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