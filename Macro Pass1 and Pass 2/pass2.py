import re
import time
from tables import MacroNameTable, MacroDataTable, AlaTable
f = open("out.txt", "r")

lines = f.readlines()


nala = {}
for lineno in range(0, len(lines)):
	line = lines[lineno].lower()
	x = re.split(r'[,\s]+', line)
	x.pop()
	linedone = False
	for j in range(0, len(x)):
		word = x[j].lower()
		if(word == ' ' or word == ''):
			continue

		for m in range(0, len(MacroNameTable)):
			#macro call
			if(MacroNameTable[m]["name"] == word):
				#print(word)
				linedone = True
				nala[word] = list()
				nala[word].append(AlaTable[word][0])
				mdtp = MacroNameTable[m]["MOT index"]
				#print(mdtp)

				#substitute variables
				for k in range(j + 1, len(x)):
					nala[word].append(x[k])

				for k in range(0, len(MacroDataTable)):
					newline = ""
					if(mdtp == MacroDataTable[k]["index"]):
							if(AlaTable[word][0] != None):
								newline += AlaTable[word][0] + " "						
							newline += word + " "
							for kl in range(j + 1, len(x)):
								newline += x[kl]
								if(kl != len(x) - 1):
									newline += ','
								
					elif(mdtp < MacroDataTable[k]["index"]):
						

						if(MacroDataTable[k]["line"] == "mend"):
							break
						linehere = MacroDataTable[k]["line"]
						lineheresplit = re.split(r'[,\s]+', linehere)

						# print(lineheresplit)
						for n in range(0, len(lineheresplit)):
							wordhere = lineheresplit[n]
							if(len(wordhere) == 0):
								continue
							elif(lineheresplit[n][0] == '#'):
								indexval = int(lineheresplit[n][1])
								# print(indexval)
								newline += nala[word][indexval] + " "
							else:
								if(wordhere.isnumeric()):
									newline += wordhere + " , "
								else:
									newline += wordhere + " "

										
					print(newline)
				
	if(linedone == False):
		print(lines[lineno])
				



print(nala)
