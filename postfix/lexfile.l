%{
#include <stdio.h>
#include <stdlib.h>
#include "y.tab.h"  // Required for token and yylval
%}

%%

[0-9]+           { yylval.val = atoi(yytext); return DIGIT; }
[a-z][a-zA-Z]*   { return ID; }
[ \t]+           ;         // Ignore spaces and tabs
\n               ;         // Ignore newlines or handle separately if needed
.                { return yytext[0]; } // Return operators as characters

%%

