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


int countSundays(int year, int endYear, int months[], int overflow = 2) {

    int days, sundays = 0;


    // Add overflow to January
    months[0] = months[0] + overflow;

    while (year <= endYear) {
        for (int month = 0; month < 12; month++) {
            if (sundayStart(months[month], isLeapYear(year)))
                sundays++;
            while (months[month] > 0)
                days = months[month];
                days -= 7;
            overflow = months[month] * -1;

            if (month < 12)
                months[month+1] = months[month+1] + overflow;
            else
                countSundays(year+1, endYear, months, overflow);
            
        }
    }

    return sundays;
}


int main() {

    int startYear = 1901,
        endYear = 2000,
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

    cout << "Answer found: " << countSundays(startYear, endYear, months) << endl;

    return 0;
}
