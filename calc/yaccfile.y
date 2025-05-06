%{
#include <stdio.h> 
#include <stdlib.h> 
void yyerror(char *str);
%}

%token DIGIT
%token ADD SUB MUL DIV
%token LPAREN RPAREN 

%left ADD SUB
%left MUL DIV 

%%

S: E { printf("Result: %d\n", $1); }
 ; 
 
E: E ADD E { $$ = $1 + $3; }
 | E SUB E { $$ = $1 - $3; } 
 | E MUL E { $$ = $1 * $3; }
 | E DIV E { $$ = $1 / $3; }
 | LPAREN E RPAREN { $$ = $2; }
 | DIGIT { $$ = $1; }
 ; 

%%

int main() {
  printf("Enter an expression: ");
  yyparse(); 
  return 0; 
}

void yyerror(char *str) {
  fprintf(stdout, "Error\t%s\n", str);
}
