#include <bits/stdc++.h>
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    string a,s;
    getline(cin,a);
    getline(cin,s);
    int x = stoi(a);
    for(char c : s) {
        char base = (isupper(c)? 'A' : 'a');
        if(!isalpha(c)) cout << ' ';
        else {
            int s = c - base - x;
            if(s < 0) s += 26;
            cout << (char) (base + s);
        }
    }
}