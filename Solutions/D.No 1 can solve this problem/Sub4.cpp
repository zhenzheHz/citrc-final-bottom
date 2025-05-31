#include <bits/stdc++.h>
using namespace std;
int main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    string code;
    cin >> code;
    int first_one_index = -1;
    for(int i=0;i<code.size();i++) {
        if(code[i] == '1') {
            first_one_index = i;
            break;
        }
    }
    if(first_one_index == -1) return cout<<"0",0;
    cout << 1;
    for(int i=first_one_index+1;i<code.size();i++) {
        cout << 0;
    }
    return 0;
}