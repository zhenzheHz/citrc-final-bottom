#include <bits/stdc++.h>
#define int int64_t
using namespace std;
vector<char> dict;
signed main() {
    int x,y;
    cin >> x >> y;
    if(x == 0) return cout<<0,0;
    for(int i=0;i<10;i++) dict.push_back('0'+i);
    for(int i=0;i<26;i++) dict.push_back('A'+i);
    string cv = "";
    while(x) {
        cv = dict[x%y] + cv;
        x /= y;
    }
    return cout<<cv,0;
}