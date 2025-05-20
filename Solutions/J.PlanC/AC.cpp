#include <bits/stdc++.h>
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    int a,b,c;
    cin >> a >> b >> c;
    int D = b*b-4*a*c;
    if(D < 0) return cout<<"no real root\n",0;
    double d = sqrt(D), aa = a * 2.0;
    cout << fixed << setprecision(15) << (0-b+d) / aa << '\n';
    cout << fixed << setprecision(15) << (0-b-d) / aa << '\n';
}