import re
f = open("input.txt", "r")

reg = [None for i in range(0 ,2)]

def getReg(opx):
	f = False
	c = 0
	for i in range(0 ,2):
		if(reg[i] == opx):
			f = True
			c = i			
			break
		
	if(f == False):
		for i in range (0 ,2):
			if(reg[i] == None):
				reg[i] = opx
				print("MOV " + opx + "," + "R" + str(i))
				return i
	else:
		return c


def findReg(opx):
	for i in range(0, 2):
		if(reg[i] == opx):
			return i
	return -1

val = {"+" : "ADD", "-" : "SUB", "*" : "MUL", "/" : "DIV"}

f1 = f.readlines()
for j in range(0, len(f1)):
	if(len(f1[j]) == 1):
		continue
	x = re.split(r'=', f1[j])
	left = x[0]
	right = re.split(r'([\+-/\*])', x[1])
	for i in range(0, len(right)):
		right[i] = right[i].replace('\n', '')
	var1 = right[0]
	op = right[1]
	var2 = right[2]
	c = getReg(var1)
	opval = val[op]
	reg[c] = left
	ind = findReg(var2)
	if ind == -1:
		print (opval , var2 , ", R" + str(c))
	else:
		print(opval, "R"+ str(ind), ", R"+ str(c))
	
	if (j == (len(f1) - 1)):
		print("MOV " + "R" + str(c) + ", " + left)
	
	#print(str(reg))
	for k in range(0, 2):
		if(reg[k] != None):
			print("R" + str(k) + " contains " + reg[k])
