#include <bits/stdc++.h>
#define int int64_t
static constexpr int mod = 1e9+7;
// std::unordered_map<int,int> dp;
int f(int x) {
    if(x == 1 || x == 2) return 1;
    // if(dp.find(x) != dp.end()) return dp[x];
    return (f(x-1) + f(x-2)) % mod;
}
signed main() {
    int q,n;
    std::cin>>q>>n;
    return std::cout<<f(n),0;
}