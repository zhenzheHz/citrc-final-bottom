#include <bits/stdc++.h>
using namespace std;
bool check(int x) {
    while(x) {
        if(x %10 == 1) return 1;
        x /= 10;
    }
    return 0;
}
signed main() {
    int n;
    cin >> n;
    const int iter = 1e5+5;
    for(int k=0;k<=iter;k++) {
        if(!check(n+k)) return cout<<k,0;
    }
}