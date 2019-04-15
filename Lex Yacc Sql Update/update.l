alpha [A-Za-z]
digit [0-9]
%%
[ \t\n]
UPDATE    return UPDATE;
SET    	return SET;
WHERE    return WHERE;
OR   	return OR;
AND    	return AND;
{digit}+    return NUM;
{alpha}({alpha}|{digit})*    return ID;
"<="    return LE;
">="    return GE;
"="    	return EQ;
"<>"    return NE;

.    return yytext[0];
%%
