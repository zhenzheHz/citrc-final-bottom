/*
q = B
x <= 1011
*/
#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    char q;
    int x;
    cin >> q >> x;
    for(int i=1;i<=11;i++) {
        if(i*i*i+i >= x) {
            return cout<<i-1,0;
        }
    }
}