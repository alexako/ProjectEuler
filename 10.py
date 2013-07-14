#!/bin/python

import math

def is_prime(num):
	for i in xrange(2, int(math.sqrt(num))+1):
		if not num % i:
			return False
	return True
	
def get_sum_of_primes(limit):
	primes = []
	for num in range(2, limit):
		if is_prime(num):
			primes.append(num)

	return sum(primes)
	
if __name__ == '__main__':
	print "Answer found: ", get_sum_of_primes(2000000)
