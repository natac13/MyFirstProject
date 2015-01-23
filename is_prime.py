'''My couple attempts to make a function to check if a number is prime'''


import math

#def is_prime(n):
#    if n <= 3:
#		print n >= 2
#		return n >= 2
#   if n % 2 == 0 or n % 3 == 0:
#        # return False
#   for i in range(5, int(n ** 0.5) + 1, 6):
#       if n % i == 0 or n % (i + 2) == 0:
#           return False
#   return True


#ans = 0	
#for x in range(1, 2000000):
#	if is_prime(x):
#		# ans += x
#print ans


prime_numbers = []

def prime_check(x):
	if x <= 3:
		return x >= 2   # this is to make sure it returns true if the number is 2
	elif x % 2 == 0 or x % 3 == 0:
		return False
	else:
		for i in range(5, int(math.sqrt(x)) + 1, 2):
				if x % i == 0:
					return False
	
	return True

num_to_check = 1

	
while len(prime_numbers) < 1000:
		num_to_check += 1
		if prime_check(num_to_check):
			prime_numbers.append(num_to_check)
		
print prime_numbers[-1]

