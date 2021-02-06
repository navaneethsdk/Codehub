#include "iostream"
#include <bits/stdc++.h>

using namespace std; //standard namespace

void print(vector<int> vec){
    for (int x:vec) 
        cout<<x<<" ";
    
    cout<<"\n";    
}

void insertion_sort(vector<int> vec){
    int j;
    for (int i = 0; i < vec.size(); i++)
    {
        int key = vec[i];
        j = i-1;
        while (j>=0 && vec[j]>key)
        {
            vec[j+1] = vec[j];
            j--;
        }
        vec[j+1] = key;
        
    }
    print(vec);
}

int main(void) 
{
    vector<int> vec = {11,43,2,3,55,33,88};
    print(vec);
    insertion_sort(vec); 
    return 0;
}