'''
The problem was to count vowels in a given string

returns: integer
'''

s = 'string of characters to check for vowels'

count = 0

for x in s:
	if x in 'aeiouAEIOU':
		count += 1
print count
