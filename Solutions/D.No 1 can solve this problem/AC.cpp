#include <bits/stdc++.h>
#define int int64_t
using namespace std;
using integar = string;
integar operator-(const integar &a, const integar &b) {
    const integar A(a.rbegin(),a.rend()), B(b.rbegin(),b.rend());
    vector<int> C(A.size());
    for(int i=0;i<C.size();i++) C[i] = (A[i]-'0') - (B[i]-'0');
    for(int i=0;i<C.size()-1;i++) {
        if(C[i] < 0) {
            C[i+1] -= 1;
            C[i] += 10;
        }
    }
    while(C.size() > 1 && C.back() == 0) C.pop_back();
    integar GET = "";
    reverse(C.begin(),C.end());
    for(auto digit : C) GET.push_back('0'+digit);
    return GET;
}
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    integar s, append = "";
    cin >> s;
    bool first = 0;
    for(int i=0;i<s.size();i++) {
        if(first) append.push_back('0');
        else if(s[i] == '1') first = 1,append.push_back('2');
        else append.push_back(s[i]);
    }
    if(!first) return cout<<0,0;
    integar ans = append - s;
    return cout << ans,0;
}