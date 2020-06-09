#!/usr/bin/env python3

import sys
import pickle
from pathlib import Path
from antlr4 import *
from Skyline import *
if __name__ is not None and "." in __name__:
    from .EvalVisitor import EvalVisitor, SkyilineNotAssigned
    from .SkylineParser import SkylineParser
    from .SkylineLexer import SkylineLexer
else:
    from EvalVisitor import EvalVisitor, SkyilineNotAssigned
    from SkylineParser import SkylineParser
    from SkylineLexer import SkylineLexer


class Antlr():
    def __init__(self, initialBuildings={}):
        """Class constructor"""
        self.visitor = EvalVisitor()

    def send(self, text, user_id):
        """Executes code 'text' sent bu the user 'user_id', and returns the resulting skyline measures"""
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
            ret = self.visitor.visit(tree)
            ret.saveImage(user_id)
            return True, [ret.getMeasures()]

        except SkyilineNotAssigned:
            return False, 'Variable not initialized'

        except WrongDimensions:
            return False, 'Wrong dimensions'

        except AttributeError:
            return False, 'Command not valid'

        except Exception as e:
            return False, 'Unknown error'

    def lst(self):
        """Returns the list of skyline instances"""
        return self.visitor.listKeys()

    def getArea(self, id):
        """Returns the area of skyline 'id'"""
        return self.visitor.getArea(id)

    def clean(self):
        """Clears current session data"""
        self.visitor = EvalVisitor()

    def save(self, user_id, name):
        """Saves the skyline with id 'name' for user 'user_id'"""
        if name in self.visitor.getDictionary():
            data = self.visitor.getDictionary()[name].getCompressedSkyline()
            path = str(Path(__file__).parent) + "/userData/"
            Path(path + user_id).mkdir(parents=True, exist_ok=True)
            pickle_file = open(path + user_id + '/' + name + '.sky', 'wb')
            pickle.dump(data, pickle_file)
            pickle_file.close()
            return True, None
        else:
            return False, 'Variable not initialized'

    def load(self, user_id, name):
        """Loads the skyline with id 'name' for user 'user_id'"""
        try:
            path = str(Path(__file__).parent) + "/userData/"
            pickle_file = open(path + user_id + '/' + name + '.sky', 'rb')
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
