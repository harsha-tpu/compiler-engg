%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int count = 1;
int yylex(void);
void yyerror(char *str);
%}

%union {
    char *s;
};

%token <s> ID NUM
%type <s> E T F

%%

S: STATS { printf("Valid!\n"); }
 ;

STATS: STAT STATS
     | STAT
     ;

STAT: ID '=' E {
        printf("%s = %s\n", $1, $3);
        free($1);
        free($3);
     }
     ;

E: E '+' T {
        printf("t%d = %s + %s\n", count, $1, $3);
        char temp[20];
        sprintf(temp, "t%d", count++);
        $$ = strdup(temp);
        free($1); free($3);
     }
 | E '-' T {
        printf("t%d = %s - %s\n", count, $1, $3);
        char temp[20];
        sprintf(temp, "t%d", count++);
        $$ = strdup(temp);
        free($1); free($3);
     }
 | T { $$ = $1; }
 ;

T: T '*' F {
        printf("t%d = %s * %s\n", count, $1, $3);
        char temp[20];
        sprintf(temp, "t%d", count++);
        $$ = strdup(temp);
        free($1); free($3);
     }
 | T '/' F {
        printf("t%d = %s / %s\n", count, $1, $3);
        char temp[20];
        sprintf(temp, "t%d", count++);
        $$ = strdup(temp);
        free($1); free($3);
     }
 | F { $$ = $1; }
 ;

F: '(' E ')' { $$ = $2; }
 | ID { $$ = $1; }
 | NUM { $$ = $1; }
 ;

%%

void yyerror(char *str) { printf("Error!\n");}

int main() {
	yyparse() ;
	return 0;
}


