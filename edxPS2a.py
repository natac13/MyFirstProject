balance = float(raw_input("Your credit card balance: "))
annualInterestRate = float(raw_input("Annual interest rate as a decimal: "))
monthlyPaymentRate = float(raw_input("Minimum monthly payment rate as a decimal: "))

monthlyInterestRate = annualInterestRate / 12.0
total_paid = 0

for month in range(1, 13):
	print "Month: ", month
	min_month_payment = round((balance * monthlyPaymentRate), 2)
	print "Minimum monthly payment: ", min_month_payment
	total_paid += min_month_payment
	balance -= min_month_payment
	balance += round((balance * monthlyInterestRate), 2)
	print "Remaining balance: ", balance
	
	
print "Total amount paid: ", total_paid
print "Remaining balance: ", balance