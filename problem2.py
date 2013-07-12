#!/bin/python

def fib(limit):
	num1, num2 = 1, 2
	while True:
		yield  num1
		num1, num2 = num2, num1 + num2
		if num1 > limit:
			break

if __name__ == '__main__':
	print sum([num  for num in fib(4000000) if not num % 2])
