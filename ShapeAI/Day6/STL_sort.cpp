#include "iostream"
#include <bits/stdc++.h>

using namespace std; //standard namespace

void print(vector<int> vec){
    for (int x:vec) 
        cout<<x<<" ";
    
    cout<<"\n";    
}

int main(void) 
{
    vector<int> vec = {11,43,2,3,55,33,88};
    print(vec);
    sort(vec.begin(), vec.end());// introsort = quicksort + heapsort + insertionsort (in python timsort is used ehere also insertion sort is used for smaller n)
    print(vec);   
    sort(vec.begin(), vec.end(), greater<int>());
    print(vec);   
    return 0;
}