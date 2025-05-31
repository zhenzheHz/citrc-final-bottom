#include <bits/stdc++.h>
using namespace std;
signed main() {
    int64_t x;
    int32_t y;
    cin >> x >> y;
    if(x == 0) return 0,0;
    assert(y == 2);
    string convert_to_binary = "";
    while(x) {
        convert_to_binary.append(to_string(x & 1));
        x >>= 1;
    }
    cout << string(convert_to_binary.rbegin(), convert_to_binary.rend());
}