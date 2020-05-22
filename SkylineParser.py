# Generated from Skyline.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("8\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3(\n\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\63\n\3\f\3\16\3")
        buf.write("\66\13\3\3\3\2\3\4\4\2\4\2\2\2>\2\6\3\2\2\2\4\'\3\2\2")
        buf.write("\2\6\7\5\4\3\2\7\b\7\2\2\3\b\3\3\2\2\2\t\n\b\3\1\2\n\13")
        buf.write("\7\3\2\2\13\f\5\4\3\2\f\r\7\4\2\2\r(\3\2\2\2\16\17\7\f")
        buf.write("\2\2\17(\5\4\3\13\20\21\7\r\2\2\21\22\7\5\2\2\22(\5\4")
        buf.write("\3\7\23(\7\r\2\2\24\25\7\3\2\2\25\26\7\t\2\2\26\27\7\6")
        buf.write("\2\2\27\30\7\t\2\2\30\31\7\6\2\2\31\32\7\t\2\2\32(\7\4")
        buf.write("\2\2\33\34\7\7\2\2\34\35\7\t\2\2\35\36\7\6\2\2\36\37\7")
        buf.write("\t\2\2\37 \7\6\2\2 !\7\t\2\2!\"\7\6\2\2\"#\7\t\2\2#$\7")
        buf.write("\6\2\2$%\7\t\2\2%(\7\b\2\2&(\7\t\2\2\'\t\3\2\2\2\'\16")
        buf.write("\3\2\2\2\'\20\3\2\2\2\'\23\3\2\2\2\'\24\3\2\2\2\'\33\3")
        buf.write("\2\2\2\'&\3\2\2\2(\64\3\2\2\2)*\f\n\2\2*+\7\n\2\2+\63")
        buf.write("\5\4\3\13,-\f\t\2\2-.\7\13\2\2.\63\5\4\3\n/\60\f\b\2\2")
        buf.write("\60\61\7\f\2\2\61\63\5\4\3\t\62)\3\2\2\2\62,\3\2\2\2\62")
        buf.write("/\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65")
        buf.write("\5\3\2\2\2\66\64\3\2\2\2\5\'\62\64")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':='", "','", "'{'", "'}'", 
                     "<INVALID>", "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "MUL", 
                      "MES", "MENYS", "WORD", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUM=7
    MUL=8
    MES=9
    MENYS=10
    WORD=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SkylineParser.ExprContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(SkylineParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExprContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExprContext,i)


        def MENYS(self):
            return self.getToken(SkylineParser.MENYS, 0)

        def WORD(self):
            return self.getToken(SkylineParser.WORD, 0)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def MUL(self):
            return self.getToken(SkylineParser.MUL, 0)

        def MES(self):
            return self.getToken(SkylineParser.MES, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 8
                self.match(SkylineParser.T__0)
                self.state = 9
                self.expr(0)
                self.state = 10
                self.match(SkylineParser.T__1)
                pass

            elif la_ == 2:
                self.state = 12
                self.match(SkylineParser.MENYS)
                self.state = 13
                self.expr(9)
                pass

            elif la_ == 3:
                self.state = 14
                self.match(SkylineParser.WORD)
                self.state = 15
                self.match(SkylineParser.T__2)
                self.state = 16
                self.expr(5)
                pass

            elif la_ == 4:
                self.state = 17
                self.match(SkylineParser.WORD)
                pass

            elif la_ == 5:
                self.state = 18
                self.match(SkylineParser.T__0)
                self.state = 19
                self.match(SkylineParser.NUM)
                self.state = 20
                self.match(SkylineParser.T__3)
                self.state = 21
                self.match(SkylineParser.NUM)
                self.state = 22
                self.match(SkylineParser.T__3)
                self.state = 23
                self.match(SkylineParser.NUM)
                self.state = 24
                self.match(SkylineParser.T__1)
                pass

            elif la_ == 6:
                self.state = 25
                self.match(SkylineParser.T__4)
                self.state = 26
                self.match(SkylineParser.NUM)
                self.state = 27
                self.match(SkylineParser.T__3)
                self.state = 28
                self.match(SkylineParser.NUM)
                self.state = 29
                self.match(SkylineParser.T__3)
                self.state = 30
                self.match(SkylineParser.NUM)
                self.state = 31
                self.match(SkylineParser.T__3)
                self.state = 32
                self.match(SkylineParser.NUM)
                self.state = 33
                self.match(SkylineParser.T__3)
                self.state = 34
                self.match(SkylineParser.NUM)
                self.state = 35
                self.match(SkylineParser.T__5)
                pass

            elif la_ == 7:
                self.state = 36
                self.match(SkylineParser.NUM)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 40
                        self.match(SkylineParser.MUL)
                        self.state = 41
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 43
                        self.match(SkylineParser.MES)
                        self.state = 44
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 46
                        self.match(SkylineParser.MENYS)
                        self.state = 47
                        self.expr(7)
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




