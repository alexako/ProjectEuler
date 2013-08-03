#!/bin/python


def isLeapYear(year):
    if (not year % 100) and year % 400:
        return False
    return not year % 4


def countSundays():

    counter = 0 # Counts the months that start on a sunday

    for month in xrange(12):
        day = start_day[month]
        for year in xrange(1901, 2001):
            if day == 0:
                counter += 1
#                print "Year: ", year, "Month: ", month
            if isLeapYear(year):
                if day >= 6:
                    day = 0
                else:
                    day += 1

            if day < 6:
                day += 1
            else:
                day = 0
            
    return counter


if __name__ == '__main__':

    # Day of week each month starts in 1901 respectively
    start_day = [2, 5, 5, 1, 3, 6, 1, 4, 0, 2, 5, 0]

    print "Answer found: ", countSundays()
