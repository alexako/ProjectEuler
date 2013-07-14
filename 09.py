#!/bin/python

# Conditions:
# a < b < c
# a^2 + b^2 = c^2

# Goal: a + b + c = 1000; Find product of abc
# Example: 3^2 + 4^2 = 9 + 16 = 25 = 5^2

def find_pythagorean_triplet(num):
	for n in range(2, num):
		for m in range(1, n):
			a, b, c = (n**2 - m**2), (2 * n * m), (n**2 + m**2)
			if a + b + c == num:
				return a * b * c
	
if __name__ == '__main__':
	print "Answer found: ",	find_pythagorean_triplet(1000)
