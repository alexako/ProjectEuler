#include <iostream>

using namespace std;


int divisorSum(int num) {

    int sum = 0;

    for (int n = 0; n < num; n++) {
        if (!(num % n))
            sum += n;
    }

    return sum;
}


int amicablePair(int limit) {

    int sum = 0;

    for (int i = 10; i < limit; i++) {

    for (int j = 10; j < limit; i++) {
       if ((divisorSum(i) == divisorSum(j)) && (i != j)) {
           sum += divisorSum(i);
        }
    }


    return sum;
}

int main() {

    int limit = 10000;

    cout << "Answer found: " << amicablePair(limit) << endl;

    return 0;
}
