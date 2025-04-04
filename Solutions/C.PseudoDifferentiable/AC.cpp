#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    vector<int> cof(n+1);
    for(int &i : cof) cin >> i;
    reverse(cof.begin(),cof.end());
    for(int i=1;i<cof.size();i++) {
        cof[i] *= i;
    }
    reverse(cof.begin(),cof.end());
    cof.pop_back();
    for(int &i : cof) cout << i << " ";
    return 0;
}