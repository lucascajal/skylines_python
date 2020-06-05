# Generated from Skyline.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("S\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3 \n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\7\3+\n\3\f\3\16\3.\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4B\n\4")
        buf.write("\3\5\3\5\3\5\3\5\7\5H\n\5\f\5\16\5K\13\5\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\2\3\4\b\2\4\6\b\n\f\2\2\2W\2\16\3\2\2\2")
        buf.write("\4\37\3\2\2\2\6A\3\2\2\2\bC\3\2\2\2\nN\3\2\2\2\fP\3\2")
        buf.write("\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21\22\b")
        buf.write("\3\1\2\22\23\7\3\2\2\23\24\5\4\3\2\24\25\7\4\2\2\25 \3")
        buf.write("\2\2\2\26\27\7\16\2\2\27 \5\4\3\13\30\31\7\17\2\2\31\32")
        buf.write("\7\5\2\2\32 \5\4\3\7\33 \5\n\6\2\34 \5\b\5\2\35 \5\6\4")
        buf.write("\2\36 \5\f\7\2\37\21\3\2\2\2\37\26\3\2\2\2\37\30\3\2\2")
        buf.write("\2\37\33\3\2\2\2\37\34\3\2\2\2\37\35\3\2\2\2\37\36\3\2")
        buf.write("\2\2 ,\3\2\2\2!\"\f\n\2\2\"#\7\f\2\2#+\5\4\3\13$%\f\t")
        buf.write("\2\2%&\7\r\2\2&+\5\4\3\n\'(\f\b\2\2()\7\16\2\2)+\5\4\3")
        buf.write("\t*!\3\2\2\2*$\3\2\2\2*\'\3\2\2\2+.\3\2\2\2,*\3\2\2\2")
        buf.write(",-\3\2\2\2-\5\3\2\2\2.,\3\2\2\2/\60\7\3\2\2\60\61\7\13")
        buf.write("\2\2\61\62\7\6\2\2\62\63\7\13\2\2\63\64\7\6\2\2\64\65")
        buf.write("\7\13\2\2\65B\7\4\2\2\66\67\7\7\2\2\678\7\13\2\289\7\6")
        buf.write("\2\29:\7\13\2\2:;\7\6\2\2;<\7\13\2\2<=\7\6\2\2=>\7\13")
        buf.write("\2\2>?\7\6\2\2?@\7\13\2\2@B\7\b\2\2A/\3\2\2\2A\66\3\2")
        buf.write("\2\2B\7\3\2\2\2CD\7\t\2\2DI\5\6\4\2EF\7\6\2\2FH\5\6\4")
        buf.write("\2GE\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2K")
        buf.write("I\3\2\2\2LM\7\n\2\2M\t\3\2\2\2NO\7\17\2\2O\13\3\2\2\2")
        buf.write("PQ\7\13\2\2Q\r\3\2\2\2\7\37*,AI")
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
    RULE_number = 5

    ruleNames =  [ "root", "expr", "building", "buildings", "var", "number" ]

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
            self.state = 12
            self.expr(0)
            self.state = 13
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


        def number(self):
            return self.getTypedRuleContext(SkylineParser.NumberContext,0)


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
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 16
                self.match(SkylineParser.T__0)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.match(SkylineParser.T__1)
                pass

            elif la_ == 2:
                self.state = 20
                self.match(SkylineParser.MENYS)
                self.state = 21
                self.expr(9)
                pass

            elif la_ == 3:
                self.state = 22
                self.match(SkylineParser.WORD)
                self.state = 23
                self.match(SkylineParser.T__2)
                self.state = 24
                self.expr(5)
                pass

            elif la_ == 4:
                self.state = 25
                self.var()
                pass

            elif la_ == 5:
                self.state = 26
                self.buildings()
                pass

            elif la_ == 6:
                self.state = 27
                self.building()
                pass

            elif la_ == 7:
                self.state = 28
                self.number()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 40
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 32
                        self.match(SkylineParser.MUL)
                        self.state = 33
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 35
                        self.match(SkylineParser.MES)
                        self.state = 36
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 38
                        self.match(SkylineParser.MENYS)
                        self.state = 39
                        self.expr(7)
                        pass

             
                self.state = 44
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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(SkylineParser.T__0)
                self.state = 46
                self.match(SkylineParser.NUM)
                self.state = 47
                self.match(SkylineParser.T__3)
                self.state = 48
                self.match(SkylineParser.NUM)
                self.state = 49
                self.match(SkylineParser.T__3)
                self.state = 50
                self.match(SkylineParser.NUM)
                self.state = 51
                self.match(SkylineParser.T__1)
                pass
            elif token in [SkylineParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(SkylineParser.T__4)
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
                self.match(SkylineParser.T__3)
                self.state = 61
                self.match(SkylineParser.NUM)
                self.state = 62
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
            self.state = 65
            self.match(SkylineParser.T__6)
            self.state = 66
            self.building()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.T__3:
                self.state = 67
                self.match(SkylineParser.T__3)
                self.state = 68
                self.building()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
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
            self.state = 76
            self.match(SkylineParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = SkylineParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(SkylineParser.NUM)
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
         




