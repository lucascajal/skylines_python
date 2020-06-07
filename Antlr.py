import sys, traceback, pickle
from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from TreeVisitor import TreeVisitor
from EvalVisitor import EvalVisitor, SkyilineNotAssigned
from Skyline import *
from pathlib import Path

class Antlr():
   def __init__(self, initialBuildings={}):
      self.visitor = EvalVisitor()

   def send(self, text):
      if text[0] == '/':
         if text == '/clear':
            return False, 'Command not valid\. Did you mean /clean\?'
         return False, 'Command not valid'
      try:
         input_stream = InputStream(text)
         lexer = SkylineLexer(input_stream)
         token_stream = CommonTokenStream(lexer)
         parser = SkylineParser(token_stream)
         tree = parser.root()
         return True, [self.visitor.visit(tree)]

      except SkyilineNotAssigned:
         return False, 'Variable not initialized'

      except WrongDimensions:
         return False, 'Wrong dimensions'

      except AttributeError:
         return False, 'Command not valid'

      except Exception as e:
         traceback.print_exc()
         return False, 'Unknown error'
   
   def lst(self):
      return self.visitor.listKeys()

   def getArea(self, id):
      return self.visitor.getArea(id)
   
   def clean(self):
      self.visitor = EvalVisitor()
   
   def save(self, user_id, name):
      if name in self.visitor.getDictionary():
         data = self.visitor.getDictionary()[name].getCompressedSkyline()
         Path('/home/lucas/upc/LP/Python/userData/'+ user_id).mkdir(parents=True, exist_ok=True)
         pickle_file = open('/home/lucas/upc/LP/Python/userData/'+ user_id + '/' + name +'.sky', 'wb')
         pickle.dump(data, pickle_file)
         pickle_file.close()
         return True, None
      else:
         return False, 'Variable not initialized'
   
   def load(self, user_id, name):
      try:
         pickle_file = open('/home/lucas/upc/LP/Python/userData/' + user_id + '/'+ name +'.sky', 'rb')
         data = pickle.load(pickle_file)
         pickle_file.close()
         sk = Skyline()
         sk.uncompressSkyline(data)
         self.visitor.addToDictionary(name, sk)
         return True, None
      except FileNotFoundError as e:
         return False, 'File not found\. Type /load to see a list of avaliable files'

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