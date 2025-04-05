#include <bits/stdc++.h>
#define int int64_t
signed main() {
    int q,s;
    std::cin>>q>>s;
    assert(q == 3);
    if(s == 0) return std::cout<<0,0;
    for(int i=0;i<63;i++) {
        if((1<<i) == s) {
            std::cout << 1;
            for(int j=0;j<i;j++) {
                std::cout << 0;
            }
            return 0;
        }
    }
    return 0;
}