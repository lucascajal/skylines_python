# Generated from Skyline.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("O\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\36\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3")
        buf.write(")\n\3\f\3\16\3,\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4@\n\4\3\5\3")
        buf.write("\5\3\5\3\5\7\5F\n\5\f\5\16\5I\13\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\2\3\4\7\2\4\6\b\n\2\2\2T\2\f\3\2\2\2\4\35\3\2\2\2\6?")
        buf.write("\3\2\2\2\bA\3\2\2\2\nL\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2")
        buf.write("\3\16\3\3\2\2\2\17\20\b\3\1\2\20\21\7\3\2\2\21\22\5\4")
        buf.write("\3\2\22\23\7\4\2\2\23\36\3\2\2\2\24\25\7\16\2\2\25\36")
        buf.write("\5\4\3\13\26\27\7\17\2\2\27\30\7\5\2\2\30\36\5\4\3\7\31")
        buf.write("\36\5\n\6\2\32\36\5\b\5\2\33\36\5\6\4\2\34\36\7\13\2\2")
        buf.write("\35\17\3\2\2\2\35\24\3\2\2\2\35\26\3\2\2\2\35\31\3\2\2")
        buf.write("\2\35\32\3\2\2\2\35\33\3\2\2\2\35\34\3\2\2\2\36*\3\2\2")
        buf.write("\2\37 \f\n\2\2 !\7\f\2\2!)\5\4\3\13\"#\f\t\2\2#$\7\r\2")
        buf.write("\2$)\5\4\3\n%&\f\b\2\2&\'\7\16\2\2\')\5\4\3\t(\37\3\2")
        buf.write("\2\2(\"\3\2\2\2(%\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2")
        buf.write("\2+\5\3\2\2\2,*\3\2\2\2-.\7\3\2\2./\7\13\2\2/\60\7\6\2")
        buf.write("\2\60\61\7\13\2\2\61\62\7\6\2\2\62\63\7\13\2\2\63@\7\4")
        buf.write("\2\2\64\65\7\7\2\2\65\66\7\13\2\2\66\67\7\6\2\2\678\7")
        buf.write("\13\2\289\7\6\2\29:\7\13\2\2:;\7\6\2\2;<\7\13\2\2<=\7")
        buf.write("\6\2\2=>\7\13\2\2>@\7\b\2\2?-\3\2\2\2?\64\3\2\2\2@\7\3")
        buf.write("\2\2\2AB\7\t\2\2BG\5\6\4\2CD\7\6\2\2DF\5\6\4\2EC\3\2\2")
        buf.write("\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IG\3\2\2\2J")
        buf.write("K\7\n\2\2K\t\3\2\2\2LM\7\17\2\2M\13\3\2\2\2\7\35(*?G")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':='", "','", "'{'", "'}'", 
                     "'['", "']'", "<INVALID>", "'*'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "MUL", "MES", "MENYS", "WORD", 
                      "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_building = 2
    RULE_buildings = 3
    RULE_var = 4

    ruleNames =  [ "root", "expr", "building", "buildings", "var" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NUM=9
    MUL=10
    MES=11
    MENYS=12
    WORD=13
    WS=14

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
            self.state = 10
            self.expr(0)
            self.state = 11
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

        def var(self):
            return self.getTypedRuleContext(SkylineParser.VarContext,0)


        def buildings(self):
            return self.getTypedRuleContext(SkylineParser.BuildingsContext,0)


        def building(self):
            return self.getTypedRuleContext(SkylineParser.BuildingContext,0)


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
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 14
                self.match(SkylineParser.T__0)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(SkylineParser.T__1)
                pass

            elif la_ == 2:
                self.state = 18
                self.match(SkylineParser.MENYS)
                self.state = 19
                self.expr(9)
                pass

            elif la_ == 3:
                self.state = 20
                self.match(SkylineParser.WORD)
                self.state = 21
                self.match(SkylineParser.T__2)
                self.state = 22
                self.expr(5)
                pass

            elif la_ == 4:
                self.state = 23
                self.var()
                pass

            elif la_ == 5:
                self.state = 24
                self.buildings()
                pass

            elif la_ == 6:
                self.state = 25
                self.building()
                pass

            elif la_ == 7:
                self.state = 26
                self.match(SkylineParser.NUM)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 30
                        self.match(SkylineParser.MUL)
                        self.state = 31
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 33
                        self.match(SkylineParser.MES)
                        self.state = 34
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 36
                        self.match(SkylineParser.MENYS)
                        self.state = 37
                        self.expr(7)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BuildingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_building

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuilding" ):
                return visitor.visitBuilding(self)
            else:
                return visitor.visitChildren(self)




    def building(self):

        localctx = SkylineParser.BuildingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_building)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(SkylineParser.T__0)
                self.state = 44
                self.match(SkylineParser.NUM)
                self.state = 45
                self.match(SkylineParser.T__3)
                self.state = 46
                self.match(SkylineParser.NUM)
                self.state = 47
                self.match(SkylineParser.T__3)
                self.state = 48
                self.match(SkylineParser.NUM)
                self.state = 49
                self.match(SkylineParser.T__1)
                pass
            elif token in [SkylineParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(SkylineParser.T__4)
                self.state = 51
                self.match(SkylineParser.NUM)
                self.state = 52
                self.match(SkylineParser.T__3)
                self.state = 53
                self.match(SkylineParser.NUM)
                self.state = 54
                self.match(SkylineParser.T__3)
                self.state = 55
                self.match(SkylineParser.NUM)
                self.state = 56
                self.match(SkylineParser.T__3)
                self.state = 57
                self.match(SkylineParser.NUM)
                self.state = 58
                self.match(SkylineParser.T__3)
                self.state = 59
                self.match(SkylineParser.NUM)
                self.state = 60
                self.match(SkylineParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BuildingsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def building(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.BuildingContext)
            else:
                return self.getTypedRuleContext(SkylineParser.BuildingContext,i)


        def getRuleIndex(self):
            return SkylineParser.RULE_buildings

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuildings" ):
                return visitor.visitBuildings(self)
            else:
                return visitor.visitChildren(self)




    def buildings(self):

        localctx = SkylineParser.BuildingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_buildings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(SkylineParser.T__6)
            self.state = 64
            self.building()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.T__3:
                self.state = 65
                self.match(SkylineParser.T__3)
                self.state = 66
                self.building()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(SkylineParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(SkylineParser.WORD, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = SkylineParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(SkylineParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
         




