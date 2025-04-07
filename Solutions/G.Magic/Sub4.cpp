#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    vector<int> p(n), m(n);
    for(int &i : p) cin >> i;
    for(int &i : m) cin >> i;
    int ans = LLONG_MAX;
    for(int i=0;i<n;i++) {
        int sum = 0;
        for(int j=0;j<n;j++) {
            sum += m[j] * abs(p[j] - p[i]);
        }
        ans = min(ans, sum);
    }
    return cout<<ans,0;
}