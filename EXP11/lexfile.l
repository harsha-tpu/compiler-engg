%{
#include "y.tab.h"
#include <stdio.h>
#include <string.h>
extern int yylval; 
%}

%%

[0-9]+ { yylval = atoi(yytext); return NUMBER; }
[a-zA-Z][a-zA-Z0-9]* { yylval = strdup(yytext); return ID; }
= { return EQUALS; }
"+" { return PLUS; }
"-" { return MINUS; }
"*" { return MULTIPLY; }
"/" { return DIVIDE; }
\n { return EOL; }
[ \t] ; 

%%


