#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    string N;
    int n, maxSize = -1;
    getline(cin,N);
    n = stoi(N);
    vector<string> write(n);
    for(auto &s : write) {
        getline(cin, s);
        maxSize = max(maxSize, (int)s.size());
    }
    for(auto &s : write) {
        while(s.size() < maxSize) 
            s.push_back(' ');
    }
    for(int i=0;i<maxSize;i++) {
        for(int j=n-1;j>=0;j--) {
            cout << write[j][i];
        }
        cout << '\n';
    }
    return 0;
}