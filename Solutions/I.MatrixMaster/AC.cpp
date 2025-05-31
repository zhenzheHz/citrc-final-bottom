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
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    int n,a,b,c,d,e;
    cin >> n >> a >> b >> c >> d >> e;
    matrix T = {
        {a,b*c,d*e,0},
        {b,a,0,0},
        {d,0,a,0},
        {0,d,b,0}
    };
    matrix S = {
        {1},
        {0},
        {0},
        {0}
    };
    while(n) {
        if(n & 1) S = T * S;
        n >>= 1;
        T = T * T;
    }
    for(int i=0;i<4;i++) {
        cout << S[i][0] << " \n"[i==3];
    }
}