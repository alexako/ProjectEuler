#!/bin/python


def find_fib(digits):

    count = 1
    num1, num2 = 1, 1
    while True:
        count += 1
        num1, num2 = num2, num1 + num2
        if len(str(num1)) == digits:
            return count

if __name__ == '__main__':
    digits = 1000
    print "Answer found: ", find_fib(digits)
