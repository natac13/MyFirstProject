'''
Does the same as PS2b, which is return the min monthly payment to pay off debt in one year
Difference is that I use bi-sectional search 
This allows for larger searches.

returns: integer which is the minimun monthly payment of any amonut
'''


balance = float(raw_input("Balance?? "))
annualInterestRate = float(raw_input("Annual Interest, as decimal: "))


monthlypayment = 0
monthly_interest_rate = annualInterestRate / 12.0
test_balance = balance
low = balance / 12
high = (balance * ((1 + monthly_interest_rate) ** 12)) / 12
episilon = 0.0005


while balance != 0:
	test_balance = balance
	monthlypayment = (high + low) / 2
	
	
	
	for month in range (1, 13):
		test_balance -= monthlypayment
		test_balance += round((test_balance * monthly_interest_rate), 2)
		if test_balance <= 0:
			break
		
	if (high - low) < episilon:
		test_balance = balance
		monthlypayment = round((monthlypayment + .0049999), 2)
		for month in range (1, 13):
			test_balance -= monthlypayment
			test_balance += round((test_balance * monthly_interest_rate), 2)
				
		balance = 0
	elif test_balance < 0:
		high = monthlypayment
	else:
		low = monthlypayment
	
		

print 'Lowest Payment: ', monthlypayment
