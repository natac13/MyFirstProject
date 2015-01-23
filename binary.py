def binary_converter(x):
	assert x > 0
	binary = ''
	y = x
	while x >= 1:
		remainder = x % 2
		x /= 2
		##print "Remainder: %d ..... Num %d" % (remainder, x)
		binary = str(remainder) + binary
	print 'The binary version of %d is %s' % (y, binary[::])	
	# the binary result is building backward if not then I need [::-1} instead
		

while True:	
	binary_converter(int(raw_input('Base 10 number??:  ')))
		
		
		
