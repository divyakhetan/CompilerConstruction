import re
f = open('input.txt', "r")

macroopened = False
macrogoingon = False
mnt = []
ala ={}
mdt = []
macroname = ""

lines = f.readlines()

for lineno in range(0, len(lines)):
	line = lines[lineno].lower()
	x = re.split(r'[,\s]+', line)
	x.pop()
	lineprocessed = False
	#print(x)
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
			mdt.append(line[:-1])
			lineprocessed = True


		if(word == 'mend'):
			mdt.append(word)
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

			mdt.append(newline)
					
	elif(macrogoingon == False and lineprocessed == False and word != 'mend'):
		print(line.replace('\n', ''))

# for j in range(0, len(mnt)):
# 	print(mnt[j]["name"])
print()
print("The Macro Name Table is ")
print(mnt)
print()
print("The Macro Data Table is ")
print(mdt)
print()
print("The ALA is ")
print(ala)
