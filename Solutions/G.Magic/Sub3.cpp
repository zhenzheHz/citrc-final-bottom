#include <bits/stdc++.h>
#define int int64_t
using namespace std;
int p1,p2,p3,M1,M2,M3;
inline int calculate(int x) {
    return M1*abs(x-p1)+M2*abs(x-p2)+M3*abs(x-p3);
}
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    cin >> p1 >> p2 >> p3;
    cin >> M1 >> M2 >> M3;
    vector<int> trials = {calculate(p1), calculate(p2), calculate(p3)};
    cout << *min_element(trials.begin(), trials.end());
}