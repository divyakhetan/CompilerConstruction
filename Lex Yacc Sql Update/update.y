%{
#include <stdio.h>
#include <stdlib.h>
%}
%token LE GE EQ NE OR AND UPDATE SET WHERE NUM ID

%%
S: ST1 {printf("Input accepted.\n");exit(0);};
ST1: UPDATE ID SET E1 ';' | UPDATE ID SET E1 WHERE E2 ';';
E1: ID EQ '\''ID'\'' | ID EQ NUM | ID EQ '\''ID'\'' ',' E1 | ID EQ NUM ',' E1;
E2: E2 AND E2 | E2 OR E2 | ID '>' ID | ID '>' NUM | ID '<' ID | ID '<' NUM | ID EQ '\''ID'\'' | ID EQ NUM | ID GE ID | ID GE NUM | ID LE ID | ID LE NUM | ID NE ID | ID NE NUM ;
%%

#include "lex.yy.c"

main()
{
   printf("Enter the exp: ");
   yyparse();
}
