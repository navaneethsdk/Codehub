#include "iostream" 
#include <bits/stdc++.h>
using namespace std;

int binary_search(vector<int> res, int n, int item){
    int l = 0;
    int h = n-1;
    int m;
    while (l<=h)
    {
        m = l + (h-l)/2;
        if(res[m] == item){
            return m;
        }
        else if( res[m] <  item){
            l = m+1;
        }
        else{
            h = m-1;
        }
    }
    return -1;
}
    

int main(){
    vector<int> res = {2,4,7,9,13,21};
    int ans;
    ans= binary_search(res, 6, 7);
    
    
    cout<<"Smallest number index"<<ans<<"\n";
    
    
    return 0;
}