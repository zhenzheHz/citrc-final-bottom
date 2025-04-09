# CITRC-Bottom-Final題解

## A. Unattainable
> **首殺**
> zh

### 轉換一下問題
要拿到僅有 $x$ 份的特點 $\rightarrow$ 比第 $x$ 個人還要早到
- 對於Ａ影院
最大的（最晚的）$m$ $\rightarrow$ 第 $x$ 個人到的時間少一就是答案
- 對於Ｂ影院
最大的（最晚的）$m$ $\rightarrow$ 最大的 $m$ 使得 $f(m)<x$
--- 
### Subtask 2. 去Ａ影城且 $<t_n>$ 由小到大排序
> 目標：比第 $x$ 個人還要早到，第 $x$ 個人到的時間少一就是答案

第 $x$ 個人到的時間是 $t[x]$，所以 $t[x]-1$ 就是答案

```cpp=
for(int i=1;i<=n;i++) cin >> t[i];
cout << t[x]-1;
```
---
### Subtask 5. 去Ａ影城且 $<t_n>$ 不會照大小排
不會照大小排怎麼辦？肯定是讓他照大小排
怎麼做呢？用上課教過的 `sort`
```cpp=
for(int i=1;i<=n;i++) cin >> t[i];
sort(t+1,t+n+1);
cout << t[x]-1;
```
---
### Subtask 3. 去Ｂ影城且 $a=b=0$
$a=b=0$ 代表什麼呢？就是 $f(t)=t^2$
> 目標：找到最大的 $m$ 使得 $f(m)<x$

可以列出算式 $m^2<x$，移項之後可以得到 $m<\sqrt x$
所以就可以直接算出 $m$ 就是 $\sqrt x$ 的整數部分
1. 如果 $x$ 是完全平方數，答案就是 $\sqrt x - 1$
2. 反之，答案就是 $\lfloor\sqrt x\rfloor$
```cpp=
int ans = sqrt(x);
if(ans * ans == x) ans = ans-1;
cout << ans;
```
---
### Subtask 4. 去Ｂ影城且 $x\leq 10^8$
$x\leq 10^8$ 有什麼用呢？因為 $a,b$ 皆為正數
因此即使 $a=b=0$，只要算算看 $f(1)$ ~ $f(10^4)$ 的值就可以考慮所有時間點的人數
```cpp=
for(int i=1;i<=10000;i++) {
    int f = i * i + a * i + b;
    if(f >= x) {
        cout << i-1;
        return 0;
    }
}
```
---
### Subtask 6. 去Ｂ影城且 $x\leq 10^{18}$
若 $x$ 高達 $10^{18}$ 就沒辦法一個一個算了
那要怎麼辦呢？可以很簡單的就看出時間越久，累積的人數就會越多
> 怎麼看出來？$a\geq 0,b\geq 0$，$f(t)=t^2+at+b$ 當然 $t$ 越大值就越大

也就是說 $f(t)$ 是嚴格遞增函數，所以我們就可以對他二分搜
找到最大的 $m$ 使得 $f(m)<x$
考慮最慘的情況，$a=b=0$，也就需要考慮到 $t=10^9$
因此二分搜的範圍就是 $[1,10^9]$
以下為左開右開的二分搜寫法
```cpp=
int l = 0, r = 1e9+5;
while(l+1!=r) {
    int m = (l+r)>>1;
    if(m*m+m*a+b >= x) r = m;
    else l = m;
}
cout << l;
```
---
<font color="#00EC00">**AC Code**</font> **by Zhenzhe**
```cpp=
#include <bits/stdc++.h>
#define int int64_t
using namespace std;
signed main() {
    cin.tie(nullptr)->ios_base::sync_with_stdio(0);
    char q;
    int x;
    cin >> q;
    if(q == 'A') {
        int n;
        cin >> n >> x;
        vector<int> t(n);
        for(int &i : t) cin >> i;
        sort(t.begin(), t.end());
        cout << t[x-1]-1;
    }else {
        int a,b;
        cin >> x >> a >> b;
        int l = 0, r = 1e9+5;
        while(l+1!=r) {
            int m = (l+r)>>1;
            if(m*m+m*a+b >= x) r = m;
            else l = m;
        }
        cout << l;
        // assert(l>0);
    }
    return 0;
}
```
