import re
import time
f = open('input.txt', "r")
out = open("out.txt", "w")
tables = open("tables.py", "w")

macroopened = False
macrogoingon = False
mnt = []
mdt = []
ala ={}
macroname = ""

lines = f.readlines()
mdtindex = 0
t1 = time.time()
for lineno in range(0, len(lines)):
	line = lines[lineno].lower()
	x = re.split(r'[,\s]+', line)
	x.pop()
	lineprocessed = False
	# print(x)
	for j in range(0, len(x)):
		word = x[j].lower()
		if(word == ' ' or word == ''):
			continue
		if(macroopened == True):
			if(len(x) == 4):
				macroname = x[j + 1]
				ala[macroname] = list()
				ala[macroname].append(x[0])
			else:
				macroname = word
				ala[macroname] = list()
				ala[macroname].append(None)
				
			mnt.append({"name" : macroname, "MOT index" : len(mdt)})
			
			for ind in range(1, len(x)):
				if(x[ind][0] == '&'):
					ala[macroname].append(x[ind])

			macroopened = False
			mdt.append({"index" : mdtindex, "line" : line[:-1]})
			mdtindex += 1
			lineprocessed = True


		if(word == 'mend'):
			mdt.append({"index" : mdtindex, "line" : word})
			mdtindex += 1
			macrogoingon = False
		if(word == 'macro'):
			macroopened = True
			macrogoingon = True
		
	if(macrogoingon and lineprocessed == False):
		#print(line)
		newline = ""
		if(x[0] != 'macro'):
			for indline in range(0, len(x)):
				if(x[indline][0] == '&'):
					newline += (", #" + str(ala[macroname].index(x[indline])) + " ")
				else:
					newline += str(x[indline] + " ")

			mdt.append({"index" : mdtindex, "line" : newline})
			mdtindex += 1
	elif(macrogoingon == False and lineprocessed == False and word != 'mend'):
		print(line.replace('\n', ''))
		out.write(line.replace('\n', ''))
		out.write('\n')

# for j in range(0, len(mnt)):
# 	print(mnt[j]["name"])
print("For pass1")
t2 = time.time()
print()
print("The Macro Name Table is ")
tables.write("MacroNameTable = " + str(mnt))
print(mnt)
print()
print("The Macro Data Table is ")
tables.write("\n")
tables.write("MacroDataTable = " + str(mdt))
print(mdt)
print()
print("The ALA is ")
tables.write("\n")
tables.write("AlaTable = " + str(ala))
print(ala)
print()
print("Total time taken is " + str(t2 - t1))