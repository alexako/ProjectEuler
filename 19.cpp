#include <iostream>

using namespace std;


bool isLeapYear(int year) {
    if (year % 100 == 0 && year % 400 != 0)
        return false;
    return (year % 4 == 0);
}


bool sundayStart(int days, bool leapYear) {
    /* Checks if month starts on a Sunday
     *  31 ends on Tuesday
     *  30 "    "  Monday
     *  28 "    "  Saturday
     */


    int lastDay = days % 7;

    if (days == 31)
        return lastDay == 3;
    else if (days == 30)
        return lastDay == 2;
    else if (days == 28) {
        if (!leapYear)
            return lastDay == 7;
        else
            return lastDay == 1;
    }

    return false;
}


void countSundays(int& sundays, int year, int endYear, int months[], int overflow = 2) {
    /* January of 1901 starts on Tuesday; has an 'overflow' of 2 */
    int days;

    // Add overflow to January
    months[0] = months[0] + overflow;

    while (year <= endYear) {
        for (int month = 0; month < 12; month++) {
            if (sundayStart(months[month], isLeapYear(year)))
                sundays++;

            days = months[month];
            while (days > 0) {
                days -= 7;
            }
            overflow = days * -1;

            if (month < 11)
                months[month+1] = months[month+1] + overflow;
            else { // if end of year, add overflow to Jan of next year
                year++;
                countSundays(sundays, year, endYear, months, overflow);
            }
        }
    }
}


int main() {

    int startYear = 1901,
        endYear = 2000,
        sundays = 0,
        Jan = 31,
        Feb = 28,
        Mar = 31,
        Apr = 30,
        May = 31,
        June = 30,
        July = 31,
        Aug = 31,
        Sept = 30,
        Oct = 31,
        Nov = 30,
        Dec = 31;

    int months[] = {
        Jan,
        Feb,
        Mar,
        Apr,
        May,
        June,
        July,
        Aug,
        Sept,
        Oct,
        Nov,
        Dec
        };

    countSundays(sundays, startYear, endYear, months);

    cout << "Answer found: " << sundays << endl;

    return 0;
}
