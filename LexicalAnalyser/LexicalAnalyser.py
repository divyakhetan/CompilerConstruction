import re
import time
from bisect import bisect_left 
f = open("sample.txt", "r")
out = open("out.txt", "w")


def bin_search(a, x):
	i = bisect_left(a,x)
	return i!= len(a) and a[i] == x

def isVar(str):
	 match = re.search(r'^[a-zA-z_][a-zA-z0-9_]*', str)
	 return match is not None and match[0] == str

def isNum(str):
	match = re.search(r'[0-9]*\.?[0-9]*', str)
	return match is not None and match[0] == str

time1 = time.time()
keyword = ["int", "float", "double", "char", "void", "for", "loop", "while", "do"]
operator = ["+", "-", "/", "*", "%", "="]
specialSymbol = ["{", "}", ";", '"', "'", "[", "]", ",", "(", ")"]
predefinedFunction = ["main", "printf", "scanf"]

keyword.sort()
operator.sort()
specialSymbol.sort()
predefinedFunction.sort()

variables = []
constants = []
stringliteral = []
invalid = []

flag = False;
for line in f:
	x = re.split('([^a-zA-Z0-9\._])', line)
	print(x),
	my_iterator = iter(x)
	ansofline = ""
	quotes= "";
	for word in x:
		
		if(word == ' ' or word == "\n" or word == '' or word == "\t"):
			continue
		elif(flag == True and word != "\""):
			quotes+= word
			continue
		if bin_search(keyword, word) :
			ansofline += "<keyword#" + str(keyword.index(word)) + "> "
		elif bin_search(operator, word):
			ansofline += "<operator#" + str(operator.index(word)) + "> "
		elif bin_search(specialSymbol, word):
			if(word == "\"" and flag == False):
        			flag = True
			elif(word == "\"" and flag == True):
        			flag = False
        			if quotes in stringliteral:
          				ansofline += "<stringLiteral#>" + str(stringliteral.index(quotes)) + ">"
        			else:
          				stringliteral.append(quotes),
          				ansofline += "<stringLiteral#>" + str(stringliteral.index(quotes)) + ">"
			ansofline += "<specialSymbol#" + str(specialSymbol.index(word)) + "> " 
		elif bin_search(predefinedFunction, word):
			ansofline += "<predefinedFunction#" + str(predefinedFunction.index(word)) + "> "
		else:
			# if(word.isnumeric()):
				
			# 	if word in constants:
			# 		ansofline += "<constants#" + str(constants.index(word)) + "> "
			# 	else:
			# 		constants.append(word),
			# 		ansofline += "<constants#" + str(constants.index(word)) + "> " 
			# elif(word[0].isnumeric() == False and (word[0].isalpha or word[0] == "_")):
			# 	if word in variables:
			# 		ansofline += "<variables#" + str(variables.index(word)) + "> " 
			# 	else:
			# 		variables.append(word),
			# 		ansofline += "<variables#" + str(variables.index(word)) + "> "
			# else:
			# 	ansofline += "< error > "

			if(isVar(word)):
				if word not in variables:
					variables.append(word)
				ansofline += "<variable#" + str(variables.index(word)) + "> "
			elif isNum(word):
				if word not in constants:
					constants.append(word)
				ansofline +=  "<constant#" + str(constants.index(word)) + "> "
			else:
				if word not in invalid:
					invalid.append(word)
				ansofline += "<error#" + str(invalid.index(word)) + "> "

		
	out.write(ansofline + "\n")

time2 = time.time()
print("The contents of the variable stack is ")

for x in variables:
	print(x), 

print("The constants stack is ")

for x in constants:
	print(x), 


print("The contents of the string literal is ")

for x in stringliteral:
	print(x), 
print("time taken: " + str(time2 - time1))
