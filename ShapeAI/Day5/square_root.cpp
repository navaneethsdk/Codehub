#include "iostream" 
#include <bits/stdc++.h>
using namespace std;

int binary_search( int n){
    if(n==0|n==1){
        return 0;
    }
    int l = 1;
    int h = n;
    int m;
    while (l<=h)
    {
        m = l + (h-l)/2;
        if(n == m*m ){
            return m;
        }
        else if( n < m*m){
            h = m-1;
        }
        else{
            l = m+1;
        }
    }
    return -1;
}
    

int main(){
    int n;
    cout<<"Enter the perfect square: ";
    cin>>n;
    int ans;
    ans = binary_search(n);   
    cout<<"Square root of "<<n<<" is "<<ans<<"\n";
    return 0;
}