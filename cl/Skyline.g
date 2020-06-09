grammar Skyline;

//antlr4 -Dlanguage=Python3 -no-listener -visitor Skyline.g

// For grammar debugging:
//antlr4 -Dlanguage=Python3 -no-listener Skyline.g

root : expr EOF ;

expr : '(' expr ')'
    | '-' expr
    | expr MUL expr
    | expr (MES | MENYS) expr
    | WORD ':=' expr
    | var
    | buildings
    | building
    | number            
    ;

building : '(' NUM ',' NUM ',' NUM ')'
    | '{' NUM ',' NUM ',' NUM ',' NUM ',' NUM '}'; 
    
buildings : '[' building (',' building)* ']' ;

var : WORD;

number : NUM;

NUM : [0-9]+    
    | '-' [0-9]+; 
MUL : '*' ;
MES : '+' ;
MENYS : '-' ;
WORD : [a-zA-Z]+ ;
WS : [ \n]+ -> skip ;