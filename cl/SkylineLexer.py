# Generated from Skyline.g by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("O\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\6\n\62\n\n\r\n\16\n")
        buf.write("\63\3\n\3\n\6\n8\n\n\r\n\16\n9\5\n<\n\n\3\13\3\13\3\f")
        buf.write("\3\f\3\r\3\r\3\16\6\16E\n\16\r\16\16\16F\3\17\6\17J\n")
        buf.write("\17\r\17\16\17K\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2\5")
        buf.write("\3\2\62;\4\2C\\c|\4\2\f\f\"\"\2S\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3")
        buf.write("\2\2\2\5!\3\2\2\2\7#\3\2\2\2\t&\3\2\2\2\13(\3\2\2\2\r")
        buf.write("*\3\2\2\2\17,\3\2\2\2\21.\3\2\2\2\23;\3\2\2\2\25=\3\2")
        buf.write("\2\2\27?\3\2\2\2\31A\3\2\2\2\33D\3\2\2\2\35I\3\2\2\2\37")
        buf.write(" \7*\2\2 \4\3\2\2\2!\"\7+\2\2\"\6\3\2\2\2#$\7<\2\2$%\7")
        buf.write("?\2\2%\b\3\2\2\2&\'\7.\2\2\'\n\3\2\2\2()\7}\2\2)\f\3\2")
        buf.write("\2\2*+\7\177\2\2+\16\3\2\2\2,-\7]\2\2-\20\3\2\2\2./\7")
        buf.write("_\2\2/\22\3\2\2\2\60\62\t\2\2\2\61\60\3\2\2\2\62\63\3")
        buf.write("\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64<\3\2\2\2\65\67\7")
        buf.write("/\2\2\668\t\2\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\2")
        buf.write("9:\3\2\2\2:<\3\2\2\2;\61\3\2\2\2;\65\3\2\2\2<\24\3\2\2")
        buf.write("\2=>\7,\2\2>\26\3\2\2\2?@\7-\2\2@\30\3\2\2\2AB\7/\2\2")
        buf.write("B\32\3\2\2\2CE\t\3\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2F")
        buf.write("G\3\2\2\2G\34\3\2\2\2HJ\t\4\2\2IH\3\2\2\2JK\3\2\2\2KI")
        buf.write("\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\b\17\2\2N\36\3\2\2\2\b")
        buf.write("\2\639;FK\3\b\2\2")
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
    T__6 = 7
    T__7 = 8
    NUM = 9
    MUL = 10
    MES = 11
    MENYS = 12
    WORD = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "':='", "','", "'{'", "'}'", "'['", "']'", "'*'", 
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MUL", "MES", "MENYS", "WORD", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "NUM", "MUL", "MES", "MENYS", "WORD", "WS" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


