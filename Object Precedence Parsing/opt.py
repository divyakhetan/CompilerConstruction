import re
from precedence_table import t
print("Enter input")
e = input()
e = "$" + e + "$"
grammar = "E->E+E|E*E|(E)|x"
sep = re.split(r'[->]+', grammar)
leftside = sep[0]
rightside = re.split(r'[|]+', sep[1])
terminals = ["x"]
operators = ["+", "*", "/", "^", "-", "(", ")"]
print(rightside)
print(e)
ans = ""
for j in range(1, len(e)):
	right= e[j]
	left = e[j - 1]
	#print(left + " " + right)
	order = t[left][right]
	if(order == -1):
		ans += left + "<"
	elif(order == 1):
		ans += left + ">"
	elif(order == 2):
		ans += left + "="
ans += "$"

print(ans)

stack = list()
stack.append("$")
i = 1
temp = e
while(True):
	symbol = e[i]
	if(stack[-1] == "$" and symbol == "$"):
		break
	else:
		a = stack[-1]
		b = symbol
		order = t[a][b]
		if(order == -1 or order == 2):
			stack.append(b)
			i += 1
		elif (order == 1):
			latest = stack[-1]
			stack.pop()
			top = stack[-1]
			
			while(t[latest][top] == -1):
				latest = stack[-1]
				stack.pop()
				top = stack[-1]
			print("reduced " + latest)
			if latest in terminals:
				print(leftside + "->" + latest)
				ind = temp.find(latest)
				temp = temp.replace(latest, leftside, 1)
				
			elif latest in operators:
				print(leftside + "->" + leftside + latest + leftside)
				ind = temp.find(latest)
				a = temp[ind-1] + temp[ind] + temp[ind + 1]
				temp = temp.replace(a, leftside, 1)
			print(temp)
		else:
			print("no solution")	
