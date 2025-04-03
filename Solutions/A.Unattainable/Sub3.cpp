#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    char q;
    int x,a,b;
    cin >> q >> x >> a >> b;
    int k = sqrt(x);
    assert(a == 0 && b == 0);
    if(k * k == x) k -= 1;
    return cout<<k,0;
}