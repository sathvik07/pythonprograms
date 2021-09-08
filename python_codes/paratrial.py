# Python3 code to find length of
# longest balanced parentheses prefix.

# Function to return the length of
# longest balanced parentheses prefix.
def maxbalancedprefix (str, n):
	_sum = 0
	maxi = 0
	
	# Traversing the string.
	for i in range(n):
	
		# If open bracket add 1 to sum.
		if str[i] == '(':
			_sum += 1
		
		# If closed bracket subtract 1
		# from sum
		else:
			_sum -= 1
		
	# if first bracket is closing bracket
	# then this condition would help
		if _sum < 0:
			break
			
		# If sum is 0, store the
		# index value.
		if _sum == 0:
			maxi = i + 1
	return maxi
	

# Driver Code
str = '(()'
n = len(str)
print(maxbalancedprefix (str, n))

# This code is contributed by "Abhishek Sharma 44"

