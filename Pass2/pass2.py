import re
from tables import SymbolTable, LiteralTable, LineTable
from motpot import mot, pot 
f = open("out.txt", "r")



lc = 0
basetable = [0 for i in range(0, 16)]
existinbasetable = [False for i in range(0, 16)]

def findNearest(ea):
	min = 1000000
	register = 0
	for i in range(0, 16):
		if(existinbasetable[i] and min > abs(ea - basetable[i])):
			min = abs(ea - basetable[i])
			ans = basetable[i]
			register = i
	return ans, register

lineno = 1
for line in f:
	#print("lineno " + str(lineno) )
	x = re.split(r'[,\s]+', line)
	x.pop()
	for j in range(0, len(x)):


		word = x[j].lower()
		if(word == ' ' or word == ''):
			continue

		if(word == 'ltorg' or word == 'end'):
			linenohere = lineno
			for literals in range(0, len(LiteralTable)):
						if(LiteralTable[literals]["lineno"] == linenohere):
							print(str(LiteralTable[literals]["value"]) + " " + str(LiteralTable[literals]["literal"]))
		if(word in pot):
			for m in range(0, len(LineTable)):
				if(LineTable[m]["lineno"] == lineno):
					#print("found")
					lcvalue = LineTable[m]["lc"]

			if(word == 'start'):
				lc = int(x[j + 1])
				j += 1
			elif(word == 'using'):
				val_of_arg1 = -1
				val_of_arg2 = -1
				arg1 = x[j + 1].lower()
				arg2 = x[j + 2].lower()
				if(arg1 == '*'):
					val_of_arg1 = lc
				else:
					for symbols in range(0, len(SymbolTable)):
						if(SymbolTable[symbols]["symbol"] == arg1):
							val_of_arg1 = SymbolTable[symbols]["value"]
					if(arg2.isnumeric()):
						val_of_arg2 = int(arg2)
					else:
						for symbols in range(0, len(SymbolTable)):
							if(SymbolTable[symbols]["symbol"] == arg2):
								val_of_arg2 = SymbolTable[symbols]["value"]

				#print(str(val_of_arg2) + "at " + word)
				basetable[val_of_arg2] = val_of_arg1
				existinbasetable[val_of_arg2] = True
			elif(word == 'ds'):
				print (str(lcvalue) +  " ------- " )

			elif(word == 'dc'):
				for k in range(j + 2, len(x)):
							ar = re.split(r'([^0-9])', x[k])
							for kl in ar:
								if(kl.isnumeric()):
									print(str(lcvalue) + " " + kl)
									lcvalue += 4
		elif(word in mot):
			for m in range(0, len(LineTable)):
				if(LineTable[m]["lineno"] == lineno):
					#print("found")
					lcvalue = LineTable[m]["lc"]

			if(mot[word]["type"] == 'rx'):
				if(word == "bne"):
					if(x[j + 1].isnumeric()):
						arg1 = int(x[j+1])
					else:
						insymbol = False
						for symbols in range(0, len(SymbolTable)):
							if(SymbolTable[symbols]["symbol"] == x[j + 1].lower()):
								arg1 = SymbolTable[symbols]["value"]
								insymbol = True
						if(insymbol == False):
							for literals in range(0, len(LiteralTable)):
								if(LiteralTable[literals]["literal"] == x[j + 1].lower()):
									arg1 = LiteralTable[literals]["value"]
						cbr, base = findNearest(arg1)
						index  = 0
					print(str(lcvalue) + ' bc 7 , ' + str(arg1 - cbr) + "( " + str(index) + " , " + str(base) + " )")
					continue


				if(x[j + 1].isnumeric()):
					arg1 = int(x[j+1])
				else:
					insymbol = False
					for symbols in range(0, len(SymbolTable)):
						if(SymbolTable[symbols]["symbol"] == x[j + 1].lower()):
							arg1 = SymbolTable[symbols]["value"]
							insymbol = True
					if(insymbol == False):
						for literals in range(0, len(LiteralTable)):
							if(LiteralTable[literals]["literal"] == x[j + 1].lower()):
								arg1 = LiteralTable[literals]["value"]
				
				ea = 0 
				xsplit = re.split(r'([()])+',x[j + 2])
				index = False

				actualword= ""
				for k in range (0, len(xsplit)):
					if(xsplit[k].lower() == 'index'):
						actualword = xsplit[k - 2]
						index = True
				#print(xsplit)

				indexvalue = 0
				if(index == True):
					x[j + 2] = actualword
					#print(actualword)
					for symbols in range(0, len(SymbolTable)):
						if(SymbolTable[symbols]["symbol"] == 'index'):
							indexvalue = SymbolTable[symbols]["value"]
				

				if(x[j + 2].isnumeric()):
					ea = int(x[j+2])
				else:
					insymbol = False
					for symbols in range(0, len(SymbolTable)):
						if(SymbolTable[symbols]["symbol"] == x[j + 2].lower()):
							ea = SymbolTable[symbols]["value"]
							insymbol = True

					if(insymbol == False):
						for literals in range(0, len(LiteralTable)):
							if(LiteralTable[literals]["literal"] == x[j + 2].lower()):
								ea = LiteralTable[literals]["value"]

				#print(ea)
				cbr, base = findNearest(ea)
				#print(x[j + 2])
				#print(basetable)
				#print(str(ea) + " " + str(base))

				d = ea - cbr
				
				#if(word == 'la' or word == 'l' or word == 'a' or word == 'st' or word == 'c'):
				print(str(lcvalue) + " " + word + "  " + str(arg1) + " , " + str(d) + "  ( " + str(indexvalue) + " " + str(base) + "  )" )
				
			elif(mot[word]["type"] == 'rr'):
				if(word == "br"):
					if(x[j + 1].isnumeric()):
						arg1 = int(x[j+1])
					else:
						insymbol = False
						for symbols in range(0, len(SymbolTable)):
							if(SymbolTable[symbols]["symbol"] == x[j + 1].lower()):
								arg1 = SymbolTable[symbols]["value"]
								insymbol = True
						if(insymbol == False):
							for literals in range(0, len(LiteralTable)):
								if(LiteralTable[literals]["literal"] == x[j + 1].lower()):
									arg1 = LiteralTable[literals]["value"]
					print(str(lcvalue)+ ' bcr 15 , ' + str(arg1))
					continue

				if(x[j + 1].isnumeric()):
					arg1 = int(x[j+1])
				else:
					insymbol = False
					for symbols in range(0, len(SymbolTable)):
						if(SymbolTable[symbols]["symbol"] == x[j + 1].lower()):
							arg1 = SymbolTable[symbols]["value"]
							insymbol = True
					if(insymbol == False):
						for literals in range(0, len(LiteralTable)):
							if(LiteralTable[literals]["literal"] == x[j + 1].lower()):
								arg1 = LiteralTable[literals]["value"]

				
				ea = 0 
				if(x[j +2].isnumeric()):
					ea = int(x[j+1])
				else:
					insymbol = False
					for symbols in range(0, len(SymbolTable)):
						if(SymbolTable[symbols]["symbol"] == x[j + 2].lower()):
							ea = SymbolTable[symbols]["value"]
					if(insymbol == False):
						for literals in range(0, len(LiteralTable)):
							if(LiteralTable[literals]["literal"] == x[j + 2].lower()):
								ea = LiteralTable[literals]["value"]
				print(str(lcvalue) + " " + word + " " + str(arg1) + " " + str(ea))

			lc += int(mot[word]["length"])

	lineno+=1
					

print(basetable)						

