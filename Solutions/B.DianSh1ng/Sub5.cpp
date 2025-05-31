#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    assert(n == 2);
    string s1, s2;
    cin >> s1 >> s2;
    for(int i=0;i<max(s1.size(),s2.size());i++) {
        cout << (i < s2.size()? s2[i] : ' ');
        cout << (i < s1.size()? s1[i] : ' ');
        cout << '\n';
    }
    return 0;
}