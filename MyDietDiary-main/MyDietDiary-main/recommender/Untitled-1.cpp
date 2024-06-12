#include <bits/stdc++.h>
using namespace std;
#define lli long long int

int required_days(int sum, vector<int> &array_prime) {
    vector<vector<int>> update_count(array_prime.size() + 1, vector<int>(sum + 1, 0));

    for (int i = 0; i <= sum; i++) {
        update_count[0][i] = INT_MAX - 1; // initiate the dp array with the maximum value
    }

    for (int i = 1; i <= array_prime.size(); i++) {
        for (int k = 1; k <= sum; ++k) { // here k is the required sum iterator
            // the logic behind the loops is if the array_prime value is larger than k, then the recent number is not considerable
            // the minimum count value can be equal by considering the last value that is already calculated
            if (array_prime[i - 1] > k) {
                update_count[i][k] = update_count[i - 1][k];
            } else {
                // let's take an option where we are considering the recent value, then we have to reduce the value from the required sum, hence sum is equal to sum - value and increment the count value by when we are not considering the recent value, then we will try for a smaller value and consider the last calculated value and repeat this process again
                update_count[i][k] = min(update_count[i - 1][k], update_count[i][k - array_prime[i - 1]] + 1);
                // As in the standard dp question we choose the minimum value from both the choices, we do here the same.
            }
        }
    }

    if (update_count[array_prime.size()][sum] == INT_MAX - 1) // this is the condition to check if the sum is possible or not
        return -1;
    else
        return update_count[array_prime.size()][sum]; // returning the minimum days.
}

int main() {
    int target, k;
    cin >> target;
    cin >> k;

    vector<int> array_prime;
    int check_prime = 2;
    int x = k;

    while (true) {
        bool y = false;

        for (int i = 2; i <= sqrt(check_prime); i++) {
            // if the number is divisible then it is not prime
            if (check_prime % i == 0) {
                y = true;
                break;
            }
        }

        if (y == false) // if y == false then the number is prime otherwise not
        {
            array_prime.push_back(check_prime); // push the current number to array_prime
            x--;
        }
        check_prime++;
        if (x <= 0)
            break;
    }

    int mininum_required_days = required_days(target, array_prime); // dynamic programic function called required_days

    cout << mininum_required_days;

    return 0;
}
