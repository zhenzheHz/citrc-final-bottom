#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    char q;
    int x,n;
    cin >> q >> x;
    if(q == 'A') {
        cin >> n;
        vector<int> t(n);
        for(int &i : t) cin >> i;
        sort(t.begin(), t.end());
        cout << t[x-1]-1;
    }else {
        int l = 0, r = (1<<20);
        while(l+1!=r) {
            int m = (l+r)>>1;
            if(m*m*m+m >= x) r = m;
            else l = m;
        }
        cout << l;
    }
    return 0;
}