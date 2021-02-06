#include "iostream" 
#include <bits/stdc++.h>
using namespace std;

vector<int> leader(int n, int arr[]){
    int big =0;
    vector<int> res;
    for (int i = n-1; i >= 0; i--)
    {
        if(arr[i]>=big){
            big = arr[i];
            res.push_back(big);
        }
    }
    reverse(res.begin(), res.end()); //note : res.end() returns pointer to the next block of the end 
    return res;
}

int main(){
    int arr[] = {4,2,4,7,9,3};
    vector<int> res;
    res = leader(6,arr);
    for (int i = 0; i < res.size(); i++)
    {
        cout<<res[i]<<"\n";
    }
    
    return 0;
}