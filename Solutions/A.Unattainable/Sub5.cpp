/*
q = B
*/
#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    char q;int x;
    cin >> q >> x;
    int l = 0, r = (1<<20);
    while(l+1!=r) {
        int m = (l+r)>>1;
        if(m*m*m+m >= x) r = m;
        else l = m;
    }
    cout << l;
    return 0;
}