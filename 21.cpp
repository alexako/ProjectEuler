#include <iostream>

using namespace std;


int divisorSum(int num) {

    int sum = 0;

    for (int n = 0; n < num/2 + 1; n++) {
        if (!(num % n))
            sum += n;
    }

    return sum;
}


int amicablePair(int limit) {

    int sum = 0, pairs[2][limit];

    // Store sum of divisors
    for (int i = 0; i < limit - 1; i++) {
        for (int j = 0; j < limit - 1; j++) {
            pairs[0][i+1] = i+1;
            pairs[1][j+1] = divisorSum(i+1);
        }
    }

    // Iterate list and find pairs
    for (int num = 0; num < limit; num++) {
        if (pairs[1][num] == num && pairs[0][num] != num)
            sum += num;
    }

    return sum;
}

int main() {

    int limit = 10000;

    cout << "Answer found: " << amicablePair(limit) << endl;

    return 0;
}
