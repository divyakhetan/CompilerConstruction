import re
# remove left recursion
# A -> Aa|b gives
# A -> bA'
# A' -> eps|aA'

f = open('input.txt', 'r')

for lines in f.readlines():
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
		# print(ans)
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