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
    vector<int> v;
    for(int i=0;i<n;i++) {
        for(int j=0;j<m[i];j++) {
            v.push_back(p[i]);
        }
    }
    sort(v.begin(), v.end());
    int k = (v.size() + 1) / 2;
    int x = v[k-1];
    int ans = 0;
    for(int i=0;i<n;i++) {
        ans += m[i] * abs(x - p[i]);
    }
    return cout<<ans,0;
}