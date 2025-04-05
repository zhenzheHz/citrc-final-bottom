#include <bits/stdc++.h>
int main() {
    int x;
    std::string s;
    std::cin >> x >> s;
    for(char c : s) {
        char base = (isupper(c)? 'A' : 'a');
        int s = c - base - x;
        if(s < 0) s += 26;
        std::cout << (char) (base + s);
    }
}