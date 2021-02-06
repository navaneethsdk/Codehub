#include "iostream"
#include <bits/stdc++.h>

using namespace std;
//memoization not working still taking O(2^n)
int fib(int n, unordered_map<int, int> umap={}){
    if (umap.find(n) != umap.end()) 
        return umap[n];
    if (n<=2)
        return 1;
    umap[n] = fib(n-1,umap) + fib(n-2,umap);
    return umap[n];
}

int main(){
    cout<<fib(50)<<endl;
    return 0;
}
