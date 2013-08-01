#!/bin/python


def isLeapYear(year):
    if (not year % 100) and year % 400:
        return False
    return not year % 4

def countSundays():

    counter = 0

    for month in xrange(12):
        day = start_day[month]
        for year in xrange(1901, 2001):
            if isLeapYear(year):
                day += 1
            if day == 0:
                counter += 1
                print "Day: ", day, "Year: ", year, "Month: ", month
            day += 1

            if day > 6:
                day = 0

    return counter


if __name__ == '__main__':
    start_day = [2, 5, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0]
    print "Answer found: ", countSundays()
