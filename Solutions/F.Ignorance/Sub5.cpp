#include<bits/stdc++.h>
using namespace std;
int main () {
    string s;
    while(cin >> s){
        int n = s.size();
        for(int i = 0; i < n; i++){
            char b = s[i], c = b - 2;
            if(b == 'a') cout << 'y';
            else if(b == 'b') cout << 'z';
            else if(b == 'A') cout << 'Y';
            else if(b == 'B') cout << 'Z';
            else cout << c;
        }
        cout << ' ';
    }
}