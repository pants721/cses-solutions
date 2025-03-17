#include <algorithm>
#include <bits/stdc++.h>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

vector<int> solve(vector<int> &prices, vector<int> &maxes) {
    multiset<int> max_prices;

    for (int i = 0; i < prices.size(); i++) {
        max_prices.insert(prices[i]);
    }

    vector<int> ans(maxes.size());

    for (int i = 0; i < maxes.size(); i++) {
        int curr_max = maxes[i];

        multiset<int>::iterator it = max_prices.upper_bound(curr_max);

        if (it == max_prices.begin()) {
            ans[i] = -1;
        } else {
            it--;
            ans[i] = (*it);
            max_prices.erase(it);
        }
    }

    return ans;
}

vector<string> split_string(const string& str) {
    stringstream ss(str);
    string token;
    vector<string> result;

    while (ss >> token) {
        result.push_back(token);
    }

    return result;
}

int main() {
    string l1, l2, l3;
    getline(cin, l1);
    getline(cin, l2);
    getline(cin, l3);

    vector<string> l2_words = split_string(l2);
    vector<int> prices;
    transform(l2_words.begin(), l2_words.end(), back_inserter(prices), 
              [](const string &s) { return stoi(s); });

    vector<string> l3_words = split_string(l3);
    vector<int> maxes;
    transform(l3_words.begin(), l3_words.end(), back_inserter(maxes), 
              [](const string &s) { return stoi(s); });

    vector<int> res = solve(prices, maxes);

    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << endl;
    }
}
