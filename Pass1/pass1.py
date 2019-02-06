import re
f = open("samplePass1.txt", "r")
from motpot import mot, pot
out = open("out.txt", "w")

#mot = ["LA", "SR", "L", "AR", "A", "ST", "C", "CR", "BR"]
#pot = ["START", "USING", "EQU", "LTORG"]

lc = 0
symboltable = []
literaltable = []
start = False
for line in f:
	print(lc)
	x = re.split(r'[,\s]+', line)
	#print(x)
	i = 0
	found = False	
	for j in range(0, len(x)):
		
		word = x[j].lower()
		if(word == 'start'):
			lc = int(x[j + 1])
			j += 1
		if(word == ' ' or word == ''):
			continue
		if(i == 0):
			i+=1
			if(word in pot):
				if(word == 'using' or word == 'drop'):
					
					continue
				elif(word == 'ltorg'):
					lc = lc + (8 - (lc % 8))
					for literals in range(0, len(literaltable)):
						if(literaltable[literals]["value"] == None):
							#print("hi")
							literaltable[literals]["value"] = lc
							lc += 4
				elif(word == 'end'):
					for literals in range(0, len(literaltable)):
						if(literaltable[literals]["value"] == None):
							#print("hi")
							literaltable[literals]["value"] = lc
							lc += 4
				#print("in pot")
			elif(word in mot.keys()):
				lc += mot[word]["length"]
				#print("in mot")
			else:
				
				if word not in symboltable:
					if(x[j + 1].lower() == 'equ'):
						found = True
						val = lc if (x[j+2] == '*') else int(x[j+2])
						ar = "r" if(x[j + 2] == '*') else "a" 
						symboltable.append({"symbol": word, "value": val, "length": 1, "ar": ar})
						j += 2
					elif(x[j + 1].lower() == "ds"):
						symboltable.append({"symbol": word, "value": lc, "length": 4, "ar": "r"})
						val = int(x[j + 2][:-1])
						#print(val)
						lc += val*4
						j+=2
					elif(x[j + 1].lower() == "dc"):
						symboltable.append({"symbol": word, "value": lc, "length": 4, "ar": "r"})
						
						for k in range(j + 2, len(x)):
							ar = re.split(r'([^0-9])', x[k])
							for kl in ar:
								if(kl.isnumeric()):
									lc+=4
							#lc+=8000
							
					elif(x[j].lower() == "loop" or x[j + 1].lower() == "dc"):
						symboltable.append({"symbol": word, "value": lc, "length": 4, "ar": "r"})
						j += 1
                                        
					else:
						symboltable.append({"symbol": word, "value": lc, "length": 1, "ar": "r"})

				
                                        
                                                
				#print("in symbol table")

		else:
			if(word in pot):
				if(word == 'using'):
					continue
				#print("in pot")
			elif(word in mot.keys()):
				lc += mot[word]["length"]
				#print("in mot")
			elif(word[0] == '='):
				if word not in literaltable:
					literaltable.append({"literal": word, "value": None, "length": 4, "ar": "r"})
				print("in literal table")
			elif(word.isnumeric() or word == '*'):
				print("constant")
		
	if(found == False):
		out.write(line)
print(lc)
print("Symbol\t\t\tValue\t\t\tlength\t\t\tar")
for symbols in range(0, len(symboltable)):
	print(str(symboltable[symbols]["symbol"]) + "\t\t\t" + str(symboltable[symbols]["value"]) + "\t\t\t" + str(symboltable[symbols]["length"]) + "\t\t\t" + str(symboltable[symbols]["ar"])) 
print(str(symboltable))
tables = open("tables.py", "w")
tables.write("SymbolTable = " + str(symboltable))
print()
print("Literal\t\t\tValue\t\t\tlength\t\t\tar")
for literals in range(0, len(literaltable)):
	print(str(literaltable[literals]["literal"]) + "\t\t\t" + str(literaltable[literals]["value"]) + "\t\t\t" + str(literaltable[literals]["length"]) + "\t\t\t" + str(literaltable[literals]["ar"])) 

print(str(literaltable))
tables.write("\n")
tables.write("LiteralTable = " + str(literaltable))

					

