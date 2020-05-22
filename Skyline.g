grammar Skyline;

root : expr EOF ;

expr : '(' expr ')'
    | '-' expr
    | expr MUL expr
    | expr MES expr
    | expr MENYS expr
    | WORD ':=' expr
    | WORD
    | '(' NUM ',' NUM ',' NUM ')'
    | '{' NUM ',' NUM ',' NUM ',' NUM ',' NUM '}'
    | NUM
    ;

//BUILDINGS : Building ',' ;
NUM : [0-9]+ ;
MUL : '*' ;
MES : '+' ;
MENYS : '-' ;
WORD : [a-zA-Z]+ ;
WS : [ \n]+ -> skip ;