#grammar is A -> aBb
#	    B -> aaB|ba|e

ind = 0 
temp = 0 

def A(ind):
	temp = ind	
	if(s[ind] == 'a'):
		ind += 1
		x = B(ind)
		if(x["val"] == True):
			ind = x["ind"]
			if(s[ind] == 'b'):
				ind+=1
				return True
			else:
				print(s[ind] + " " + str(ind))
	return False
			
def B(ind):
	temp = ind
	if(s[ind] == 'a'):
		ind += 1
		if(s[ind] == 'a'):
			ind += 1
			x = B(ind)
			if(x["val"]):
				ind = x["ind"]
				return {"val" : True, "ind" : ind}

	else:
		#print("enetered here")
		ind = temp
		if(s[ind] == 'b'):
			ind += 1
			if(s[ind] == 'a'):
				ind+=1
	
				return {"val" : True, "ind" : ind}

	return {"val" : False, "ind" : ind}
s = input()
print(s)

print(A(ind))

