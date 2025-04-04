#include <bits/stdc++.h>
using namespace std;
signed main() {
    int n;
    cin >> n;
    vector<char> s(n);
    for(auto &c : s) cin >> c;
    reverse(s.begin(),s.end());
    for(auto c : s) cout << c;
    return 0;
}