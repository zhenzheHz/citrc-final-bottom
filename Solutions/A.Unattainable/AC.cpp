#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    char q;
    int x;
    cin >> q;
    if(q == 'A') {
        int n;
        cin >> n >> x;
        vector<int> t(n);
        for(int &i : t) cin >> i;
        sort(t.begin(), t.end());
        cout << t[x-1]-1;
    }else {
        int a,b;
        cin >> x >> a >> b;
        int l = 0, r = 1e9+5;
        while(l+1!=r) {
            int m = (l+r)>>1;
            if(m*m+m*a+b >= x) r = m;
            else l = m;
        }
        cout << l;
        assert(l>0);
    }
    return 0;
}