#include <algorithm>
#include <bits/stdc++.h>
#include <iterator>
#include <sstream>
using namespace std;
template <class T>
void print_v(vector<T> &v) { cout << "{"; for (auto x : v) cout << x << ","; cout << "\b}"; }

vector<long int> splitBySpace(const string &str) {
    stringstream ss(str);
    istream_iterator<string> begin(ss), end;
    vector<string> s = vector<string> (begin, end);
    vector<long int> nums;
    transform(s.begin(), s.end(), back_inserter(nums),
              [](const string &str)  { return stol(str); });

    return nums;
}

int main() {
    string nums_str;
    string n_str;
    getline(cin, n_str);
    getline(cin, nums_str);
    long int n = stol(n_str);
    vector<long int> nums = splitBySpace(nums_str);

    int exp_sum = n * (n + 1) / 2;
    int sum = accumulate(nums.begin(), nums.end(), 0);
    cout << abs(exp_sum - sum) << endl;
}
