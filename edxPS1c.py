
	
s = 'vfcnifdnkgdfnjkfdujfsdnnabckfdriemikvgmabdfhil'


# Need to set 2 variables one as the final and the other as the test case
# both are set to the first letter to start
test = final = s[0]
# This creates a loop as long as the string itself 
# remember len() will return 5 for a string of "abcde" buth the 'e' is at index [4]
for i in range(1, len(s)):
	# star by comparing the next character to the last one on the test case
	if s[i] >= test[-1]:
		# if so then the char will get added to the end of the test case 
		test += s[i]
		# the test case is then checked if it is the longest 
		if len(test) > len(final):
			final = test
		# after the loop goes back and reset to the next char in the string	
	# if the next character is NOT alphabetical from the last on test it passes resets back to the next character
	else:
		test = s[i]
 
print final
