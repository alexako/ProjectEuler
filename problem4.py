#!/bin/python

def find_palindrome(digits):
	start = int('1' + '0' * (digits - 1))
	end = int('1' + '0' * (digits))

	palindromes = []

	for num1 in range(start,end):
		for num2 in range(start,end):
			if str(num1 * num2) == str(num1 * num2)[::-1]:
				palindromes.append(num1 * num2)

	return palindromes

if __name__ == '__main__':
	print max(find_palindrome(3))
