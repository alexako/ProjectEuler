#!/bin/python


def count_powers(limit):

    product = 0
    count = 0
    products = []

    for num in range(2, limit + 1):
        for exp in range(2, limit + 1):
            product = num ** exp

            if product not in products:
                products.append(product)
                count += 1

    return count

if __name__ == '__main__':
    limit = 100
    print "Answer found: ", count_powers(limit)
