'''
calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months
fixed monthly payment of $10 amounts

returns: integer which is the lowestest possible payment
'''


balance = float(raw_input("Balance?? "))
annualInterestRate = float(raw_input("Annual Interest, as decimal: "))



monthlypayment = 0
monthly_interest_rate = annualInterestRate / 12.0
test_balance = balance

while test_balance > 0:
	test_balance = balance
	monthlypayment += 10
	
	for month in range (1, 13):
		test_balance -= monthlypayment
		test_balance += round((test_balance * monthly_interest_rate), 2)
		

print 'Lowest Payment: ', monthlypayment
