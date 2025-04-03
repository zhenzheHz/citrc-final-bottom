#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    char q;
    int n,x;
    cin >> q >> n >> x;
    vector<int> t(n);
    for(int &i : t) cin >> i;
    return cout<<t[x-1]-1,0;
}