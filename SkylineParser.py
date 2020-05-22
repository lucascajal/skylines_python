# Generated from Skyline.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("&\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3\26\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\7\3!\n\3\f\3\16\3$\13\3\3\3\2\3\4\4")
        buf.write("\2\4\2\2\2*\2\6\3\2\2\2\4\25\3\2\2\2\6\7\5\4\3\2\7\b\7")
        buf.write("\2\2\3\b\3\3\2\2\2\t\n\b\3\1\2\n\13\7\3\2\2\13\f\5\4\3")
        buf.write("\2\f\r\7\4\2\2\r\26\3\2\2\2\16\17\7\t\2\2\17\26\5\4\3")
        buf.write("\t\20\21\7\n\2\2\21\22\7\5\2\2\22\26\5\4\3\5\23\26\7\6")
        buf.write("\2\2\24\26\7\n\2\2\25\t\3\2\2\2\25\16\3\2\2\2\25\20\3")
        buf.write("\2\2\2\25\23\3\2\2\2\25\24\3\2\2\2\26\"\3\2\2\2\27\30")
        buf.write("\f\b\2\2\30\31\7\7\2\2\31!\5\4\3\t\32\33\f\7\2\2\33\34")
        buf.write("\7\b\2\2\34!\5\4\3\b\35\36\f\6\2\2\36\37\7\t\2\2\37!\5")
        buf.write("\4\3\7 \27\3\2\2\2 \32\3\2\2\2 \35\3\2\2\2!$\3\2\2\2\"")
        buf.write(" \3\2\2\2\"#\3\2\2\2#\5\3\2\2\2$\"\3\2\2\2\5\25 \"")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':='", "<INVALID>", "'*'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUM", "MUL", "MES", "MENYS", "WORD", "WS" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NUM=4
    MUL=5
    MES=6
    MENYS=7
    WORD=8
    WS=9

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

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

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
            self.state = 19
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
                self.expr(7)
                pass

            elif la_ == 3:
                self.state = 14
                self.match(SkylineParser.WORD)
                self.state = 15
                self.match(SkylineParser.T__2)
                self.state = 16
                self.expr(3)
                pass

            elif la_ == 4:
                self.state = 17
                self.match(SkylineParser.NUM)
                pass

            elif la_ == 5:
                self.state = 18
                self.match(SkylineParser.WORD)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 30
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 22
                        self.match(SkylineParser.MUL)
                        self.state = 23
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 24
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 25
                        self.match(SkylineParser.MES)
                        self.state = 26
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 28
                        self.match(SkylineParser.MENYS)
                        self.state = 29
                        self.expr(5)
                        pass

             
                self.state = 34
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




