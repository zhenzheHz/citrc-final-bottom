#include <bits/stdc++.h>
#define int int64_t
signed main() {
    int q,a,b,p;
    std::cin >> q >> a >> b >> p;
    const int MAXB = 1e5;
    assert(q == 1 && b <= MAXB);
    int x = 1;
    for(int i = 0; i < b; i++) {
        x *= a;
        x %= p;
    }
    return std::cout<<x,0;
}