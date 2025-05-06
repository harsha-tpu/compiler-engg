%{
#include <stdio.h>
#include <stdlib.h> 
void yyerror(char *s);
float x = 0; 
%}

%token ONE ZERO POINT

%%

L: X POINT Y { printf("%f\n", $1 + x); }
 | X { $$ = $1; printf("%d\n", $$); }
 ; 
 
X: X B { $$ = $1 * 2 + $2; }
 | B   { $$ = $1; }
 ; 
 
Y: B Y { x = $1 * 0.5 + x * 0.5; }
 | B   { x = $1 * 0.5; }
 ; 
 
B: ZERO { $$ = $1; }
 | ONE { $$ = $1; }
 ;
 
%%

int main() {
  printf("Enter the binary number: ");
  while(yyparse());
  return 0; 
}

void yyerror(char *str) {
  fprintf(stdout, "\n%s", str);
}
