#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    char q;
    int x,a,b;
    cin >> q >> x >> a >> b;
    for(int i=1;i<=10005;i++) {
        int f = i * i + a * i + b;
        if(f >= x) return cout<<i-1,0;
    }
}