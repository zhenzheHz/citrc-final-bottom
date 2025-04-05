#include <bits/stdc++.h>
#define int int64_t
static constexpr int mod = 1e9+7, N = 2e5+5;
signed main() {
    int q,n;
    std::cin>>q>>n;
    assert(q == 2);
    int dp[N];
    dp[1] = dp[2] = 1;
    for(int i=3;i<=n;i++) {
        dp[i] = (dp[i-1] + dp[i-2]) % mod;
    }
    return std::cout<<dp[n],0;
}