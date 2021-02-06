#include "iostream" 
#include <bits/stdc++.h>
using namespace std;

int binary_search(vector<int> res, int n){
    int l = 0;
    int h = n-1;
    int m;
    while (l<=h)
    {
        m = l + (h-l)/2;
        if(res[m] == 1 && (m==0 || res[m-1]==0)){
            return m;
        }
        else if( res[m] == 1){
            h = m-1;
        }
        else{
            l = m+1;
        }
    }
    return -1;
}
    

int main(){
    vector<int> res = {0,0,0,0,0,1,1,1};
    int ans;
    ans= binary_search(res, 8);
    
    
    cout<<"Smallest number index"<<ans<<"\n";
    
    
    return 0;
}