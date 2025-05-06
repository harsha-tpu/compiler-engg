%{
#include <stdio.h>
void yyerror(char *);
%}

%token NUMBER ID EQUALS PLUS MINUS MULTIPLY DIVIDE EOL 

%%

STMT_LIST: STMT_LIST STMT
         | STMT
         ; 
         
STMT: ID EQUALS EXPR EOL { printf("LDA %s\n", $1); }
    | ID EQUALS ID PLUS ID EOL { printf("LDA %s\nADD %s\nSTA %s\n", $3, $5, $1); }
    | ID EQUALS ID MINUS ID EOL { printf("LDA %s\nSUB %s\nSTA %s\n", $3, $5, $1); }
    | ID EQUALS ID MULTIPLY ID EOL { printf("LDA %s\nMUL %s\nSTA %s\n", $3, $5, $1); }
    | ID EQUALS ID DIVIDE ID EOL { printf("LDA %s\nDIV %s\nSTA %s\n", $3, $5, $1); }
    ;
    
EXPR: NUMBER
    | ID
    | EXPR PLUS EXPR { $$ = $1 + $3; }
    | EXPR MINUS EXPR  { $$ = $1 - $3; }
    | EXPR MULTIPLY EXPR { $$ = $1 * $3; }
    | EXPR DIVIDE EXPR { $$ = $1 / $3; }
    ; 
    
%%

#include "lex.yy.c"

void yyerror(char *str) {
  fprintf(stderr, "Error!");
}

int main(void) {
  yyparse(); 
  return 0;
}
