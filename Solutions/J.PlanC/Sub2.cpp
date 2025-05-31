#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    int a,b,c;
    cin >> a >> b >> c;
    int D = b * b - 4 * a * c;
    D = sqrt(D);
    cout << (D-b)/2/a << '\n';
    cout << (-D-b)/2/a;
}