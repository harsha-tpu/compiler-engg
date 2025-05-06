%{
#include <stdio.h> 
#include <stdlib.h> 
#include "y.tab.h" 
extern int yylval; 
%}

%%

[0-9]+ { yylval = atoi(yytext); return DIGIT; }
"+" { return ADD; }
"-" { return SUB; }
"*" { return MUL; }
"/" { return DIV; }
"(" { return LPAREN; }
")" { return RPAREN; }
[ \t] ; 
\n  { return 0; }
.   { return yytext[0]; }

%%
