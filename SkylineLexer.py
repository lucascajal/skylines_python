# Generated from Skyline.g by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("?\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\6")
        buf.write("\b*\n\b\r\b\16\b+\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6\f\65")
        buf.write("\n\f\r\f\16\f\66\3\r\6\r:\n\r\r\r\16\r;\3\r\3\r\2\2\16")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\3\2\5\3\2\62;\4\2C\\c|\4\2\f\f\"\"\2A\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2")
        buf.write("\2\2\7\37\3\2\2\2\t\"\3\2\2\2\13$\3\2\2\2\r&\3\2\2\2\17")
        buf.write(")\3\2\2\2\21-\3\2\2\2\23/\3\2\2\2\25\61\3\2\2\2\27\64")
        buf.write("\3\2\2\2\319\3\2\2\2\33\34\7*\2\2\34\4\3\2\2\2\35\36\7")
        buf.write("+\2\2\36\6\3\2\2\2\37 \7<\2\2 !\7?\2\2!\b\3\2\2\2\"#\7")
        buf.write(".\2\2#\n\3\2\2\2$%\7}\2\2%\f\3\2\2\2&\'\7\177\2\2\'\16")
        buf.write("\3\2\2\2(*\t\2\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2")
        buf.write("\2\2,\20\3\2\2\2-.\7,\2\2.\22\3\2\2\2/\60\7-\2\2\60\24")
        buf.write("\3\2\2\2\61\62\7/\2\2\62\26\3\2\2\2\63\65\t\3\2\2\64\63")
        buf.write("\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67")
        buf.write("\30\3\2\2\28:\t\4\2\298\3\2\2\2:;\3\2\2\2;9\3\2\2\2;<")
        buf.write("\3\2\2\2<=\3\2\2\2=>\b\r\2\2>\32\3\2\2\2\6\2+\66;\3\b")
        buf.write("\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    NUM = 7
    MUL = 8
    MES = 9
    MENYS = 10
    WORD = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "':='", "','", "'{'", "'}'", "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MUL", "MES", "MENYS", "WORD", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "NUM", 
                  "MUL", "MES", "MENYS", "WORD", "WS" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


