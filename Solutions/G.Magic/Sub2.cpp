#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    int n;
    cin >> n;
    int pa,pb,ma,mb;
    cin >> pa >> pb >> ma >> mb;
    return cout<<min(mb*abs(pa-pb), ma*abs(pa-pb)),0;
}