#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    int a,b,c;
    cin >> a >> b >> c;
    int sum = -b/a, product = c/a;
    int diff = sqrt(sum*sum-4*product);
    cout << (sum+diff)/2 << '\n';
    cout << (sum-diff)/2;
}