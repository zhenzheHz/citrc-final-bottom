#include <bits/stdc++.h>
#define int int64_t
using namespace std;
static constexpr int mod = 1e9+7;
using matrix = vector<vector<int>>;
matrix operator*(const matrix &A, const matrix &B) {
    matrix C(A.size(), vector<int> (B[0].size(),0));
    for(int k=0;k<B.size();k++) {
        for(int i=0;i<A.size();i++) {
            for(int j=0;j<B[0].size();j++) {
                C[i][j] += A[i][k] * B[k][j] % mod;
                C[i][j] %= mod;
            }
        }
    }
    return C;
}
matrix operator%(const matrix &A, const int x) {return A;}
template<class T> T fp(T a,int b,int p) {
    // if(b == 0) return 1;
    if(b == 1) return a;
    if(b & 1) return a*fp(a,b-1,p)%p;
    T half = fp(a,b>>1,p);
    return half*half%p; 
}
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    int q,a,b,p,n,s;
    cin >> q;
    if(q == 1) {
        cin >> a >> b >> p;
        cout << fp(a,b,p) % p;
    }else if(q == 2) {
        cin >> n;
        if(n == 1 || n == 2) return cout<<1,0;
        matrix status = {{1},{1}}, tr = {{1,1},{1,0}};
        matrix ans = fp(tr, n-2, mod);
        status = ans * status;
        cout << status[0][0];
    }else {
        cin >> s;
        if(s == 0) return cout<<0,0;
        vector<int> bit;
        while(s) {
            bit.push_back(s & 1);
            s >>= 1;
        }
        reverse(bit.begin(), bit.end());
        for(int &b : bit) {
            cout << b;
        }
    }
}