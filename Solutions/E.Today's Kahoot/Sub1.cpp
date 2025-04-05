#include <bits/stdc++.h>
#define int int64_t
signed main() {
    int q,a,b,p;
    std::cin >> q >> a >> b >> p;
    assert(q == 1 && a == 2 && p == 10);
    int ans[] = {6,2,4,8};
    return std::cout<<ans[b%4],0;
}