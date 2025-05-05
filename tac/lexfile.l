%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "y.tab.h"

extern YYSTYPE yylval;
%}

%%

[ \t]+                        ; // skip whitespace
[0-9]+                         { yylval.s = strdup(yytext); return NUM; }
[_a-zA-Z][_0-9a-zA-Z]*         { yylval.s = strdup(yytext); return ID; }
"="                            { yylval.s = strdup(yytext); return '='; }
"+"                            { yylval.s = strdup(yytext); return '+'; }
"-"                            { yylval.s = strdup(yytext); return '-'; }
"*"                            { yylval.s = strdup(yytext); return '*'; }
"/"                            { yylval.s = strdup(yytext); return '/'; }
"("                            { return '('; }
")"                            { return ')'; }
";"                            { return ';'; }
\n 														 { return 0; }
.                              { return yytext[0]; }

%%

