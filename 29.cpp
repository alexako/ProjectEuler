#include <iostream>
#include <cmath>        // for pow()
#include <vector>       // for vector
#include <algorithm>    // for sort()

using namespace std;


int main() {

    vector < double > products;

    // Gets powers of num**exp, 2 >= num; exp >= 100 and append to products vector
    for (double num = 2; num <= 100; num++) {
        for (double exp = 2; exp <= 100; exp++) {
            products.push_back(pow(num, exp));
        }
    }

    // Resize and remove duplicates
    vector< double >::iterator it;
    sort(products.begin(), products.end());
    it = unique(products.begin(), products.end());
    products.resize(distance(products.begin(), it));

    // Print vector size
    cout << "Answer found: " << products.size() << endl;

    return 0;
}
