/*
q = A
<t> is sorted
*/
#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    char q;int x,n;
    cin >> q >> x >> n;
    vector<int> t(n);
    for(int &i : t) cin >> i;
    cout << t[x-1]-1;
    return 0;
}