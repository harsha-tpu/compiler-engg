%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(char *str);
int yylex(void);
%}

%union {
  int val;
}

%token <val> DIGIT
%token ID
%type <val> T

%left '+' '-'
%left '*' '/'

%%

start: T { printf("\n"); };

T: T '+' T { printf("+"); }
 | T '-' T { printf("-"); }
 | T '*' T { printf("*"); }
 | T '/' T { printf("/"); }
 | DIGIT   { printf("%d", $1); }
 ;

%%

int main() {
  printf("Enter expression: ");
  yyparse();
  return 0;
}

void yyerror(char* str) {
  printf("Error: %s\n", str);
}

