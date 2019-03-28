import re
# remove left recursion
# A -> Aa|b gives
# A -> bA'
# A' -> eps|aA'

f1 = open('inputformated.txt', 'w')
f = open('input.txt', 'r')

def replace(lines):
	lines = lines.rstrip()
	x = re.split(r'[->]+', lines)
	leftside = x[0]
	rightside = re.split(r'[|]+', x[1])

	f1.write(lines + "\n")

lineslist = f.readlines()
for lineno in range(0, len(lineslist)):
	lines = lineslist[lineno]
	lines = lines.rstrip()
	x = re.split(r'[->]+', lines)
	leftside = x[0]
	rightside = re.split(r'[|]+', x[1])
	ans = ""
	for ind in range(0, len(rightside)):
		# print(rightside[ind])
		starting = rightside[ind][0] 
		eval = False
		if(starting != leftside):
			for j in range(lineno + 1, len(lineslist)):
				if(lineslist[j][0] == starting):
					eval = True
					linescomp = lineslist[j]
					linescomp = linescomp.rstrip()
					xcomp = re.split(r'[->]+', linescomp)
					leftsidecomp = xcomp[0]
					rightsidecomp = re.split(r'[|]+', xcomp[1])
					# print(rightsidecomp)
					for k in range(0, len(rightsidecomp)):
						ans += rightsidecomp[k] + rightside[ind][1:] + "|"
				

		if(eval == False):
			ans += rightside[ind] + "|"
	ans = ans[:-1]
	finalans = leftside + "->" + ans
	print(finalans)
	f1.write(finalans + "\n")

	

f1.close()
f1 = open('inputformated.txt', 'r')
print("\n")
for lines in f1.readlines():
	lines = lines.rstrip()
	x = re.split(r'[->]+', lines)
	leftside = x[0]
	rightside = re.split(r'[|]+', x[1])
	# print(leftside)
	# print(rightside)
	alpha =  list()
	beta = list()

	for val in rightside:
		if(val[0] == leftside):
			alpha.append(val[1:])
		else:
			beta.append(val)

	if(len(alpha) == 0):
		ans = leftside + "->"
		for j in rightside:
			ans += j + "|"
		ans = ans[:-1]
		print(ans)
	else:
		ans1 = ""
		for j in beta:
			ans1 += j + leftside + "'|" 
		ans1 = ans1[:-1]
		ans = leftside + "->" + ans1  
		print(ans)  	
		ans2 = ""
		for k in alpha:
			ans2 += k +  leftside + "'|" 
		ans2 += "eps"
		ans = leftside + "'->" + ans2
		print(ans)
	# print(beta)
	# print(alpha)