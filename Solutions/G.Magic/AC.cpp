#include <bits/stdc++.h>
#define int int64_t
#define p first
#define m second
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    vector<pair<int,int>> v(n);
    for(auto &i : v) cin >> i.p;
    for(auto &i : v) cin >> i.m;
    sort(v.begin(),v.end());
    vector<int> pref(n);
    pref[0] = v[0].m;
    for(int i=1;i<n;i++) pref[i] = pref[i-1] + v[i].m;
    int k = (pref.back()+1)/2;
    auto f = lower_bound(pref.begin(), pref.end(), k) - pref.begin();
    int x = v[f].p;
    // cout << k << ' ' << x << '\n';
    int ans = 0;
    for(int i=0;i<n;i++) {
        ans += v[i].m * abs(x - v[i].p);
        // cout << v[i].m << ' ' <<  abs(x - v[i].p) << "=" << v[i].m * abs(x - v[i].p) << '\n';
    }
    return cout<<ans,0;
}