#include <bits/stdc++.h>
using namespace std;
int main() {
    int64_t x, product = 1;
    int32_t y;
    cin >> x >> y;
    if(x == 0) return cout<<0,0;
    string result = "1";
    while(product < x) {
        product *= y;
        result.push_back('0');
    }
    return cout<<result,0;
}