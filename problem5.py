#!/bin/python

def get_dividers(num):
	dividers = [i for i in xrange(1,21) if not num % i]
	return dividers

def find_smallest_number(num):
	checklist = [11, 13, 14, 16, 17, 18, 19, 20]
	while True:
		if all(item in get_dividers(num) for item in checklist):
			return num
		else:
			num += 20
				
if __name__ == '__main__':
	print "Answer Found: ", find_smallest_number(20)
