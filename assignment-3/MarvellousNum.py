def ChkPrime(no):
	if no == 1 or no == 2:
		return True
	else:
		for i in range(2,int(no / 2) + 1):
			if no % i == 0:
				return False
		return True

		
"""
no = 10	
	
if no == 1 or no == 2:
	return True
else:
	for i in range(1,int(no / 2) + 1):
		if no % i == 0:
			return False
	return True
	
"""