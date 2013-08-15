#include <iostream>
#include <cmath>

using namespace std;


int findPowerSum(int power, int digits) {

    int limit = pow(9, power) * digits,
        digit[digits],
        sum = 0,
        total,
        temp;


    for (int num = 2; num < limit; num++) {

        temp = num;
        total = 0;
        // Seperate into digits and add the nth powers
        while (temp) {
            total += pow(temp % 10, power);
            temp /= 10;
        }

        // Check if sum equals digits
        if (total == num)
            sum += total;
    }


    return sum;
}


int main() {

    int power = 5, digits = 6;

    cout << "Answer found: " << findPowerSum(power, digits) << endl;

    return 0;
}
