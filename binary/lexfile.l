%{
#include <stdio.h>
#include <stdlib.h>
#include "y.tab.h"
extern int yylval;
%}

%%

0 { yylval = 0; return ZERO; }
1 { yylval = 1; return ONE; }
"." { return POINT; }
\n { return 0; }

%%
